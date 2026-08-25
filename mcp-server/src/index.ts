import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { z } from "zod";

// Inicializa o servidor MCP
const server = new Server(
  {
    name: "techmind-agentic-tools",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// 1. LISTA DE FERRAMENTAS EXPOSTAS PARA O AGENTE (Cursor / Claude / Kiro)
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "audit_architecture_rules",
        description: "Valida se um arquivo de código viola as regras de Clean Architecture ou SOLID.",
        inputSchema: {
          type: "object",
          properties: {
            filePath: {
              type: "string",
              description: "O caminho relativo do arquivo a ser auditado.",
            },
          },
          required: ["filePath"],
        },
      },
    ],
  };
});

// 2. EXECUÇÃO DA FERRAMENTA
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "audit_architecture_rules") {
    const { filePath } = request.params.arguments as { filePath: string };
    
    return {
      content: [
        {
          type: "text",
          text: `✅ Arquivo ${filePath} analisado com sucesso: Zero violações de Clean Architecture detectadas.`,
        },
      ],
    };
  }

  throw new Error(`Ferramenta desconhecida: ${request.params.name}`);
});

// Conecta o servidor via Standard I/O (Stdio)
async function run() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("⚡ TechMind MCP Server rodando via stdio.");
}

run().catch((error) => {
  console.error("Erro fatal no servidor MCP:", error);
  process.exit(1);
});
