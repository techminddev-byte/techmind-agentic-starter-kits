#!/usr/bin/env python3
"""
TECHMINDDEV - Conversation Compactor & State Distiller
Filtra ruídos de terminal, outputs de ferramentas e destila conversas para State Checkpoints.
"""

import sys
import re

CHECKPOINT_PROMPT = """
# 🚀 STATE CHECKPOINT (Sessão Limpa)

## 📌 1. Decisões Estabelecidas
- [Liste as principais decisões arquiteturais tomadas]

## 📁 2. Arquivos Modificados & Status Atual
- `caminho/arquivo.ext` -> [O que foi implementado e validado]

## 🎯 3. Próximo Objetivo Imediato
- [Qual é o próximo passo cirúrgico exato a executar]

## 🛡️ 4. Invariantes para o Agente
- Siga a arquitetura Feature-First e o PROJECT_INDEX.md.
- Mantenha respostas concisas e código abaixo de 200 linhas.
"""

def compact_log(text: str) -> str:
    """Filtra ruídos comuns de terminal e outputs massivos de compilação."""
    noise_patterns = [
        r'node_modules',
        r'Compiling\.\.\.',
        r'webpack',
        r'npm WARN',
        r'Finished task',
        r'yarn run',
        r'\[DEBUG\]',
    ]
    combined_pattern = re.compile('|'.join(noise_patterns), re.IGNORECASE)
    
    lines = text.splitlines()
    cleaned_lines = [l for l in lines if not combined_pattern.search(l)]
    return "\n".join(cleaned_lines)

def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            print("--- CONTEÚDO DESTILADO ---")
            print(compact_log(content))
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}", file=sys.stderr)
    else:
        print("Uso: python compact_conversation.py <arquivo_de_log_ou_chat.txt>")
        print("\nTemplate Canônico de Checkpoint:")
        print(CHECKPOINT_PROMPT)

if __name__ == '__main__':
    main()
