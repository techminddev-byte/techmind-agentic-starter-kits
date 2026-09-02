---
inclusion: auto
---

# 📱 04 — Versionamento Mobile & Cache-Busting (Flutter, iOS & Android)

Este documento define as regras de governança para evitar a execução de código fantasma preso em cache no mobile e web.

---

## 1. A Regra do `pubspec.yaml` no Flutter
Toda versão de aplicativo mobile Flutter deve seguir a sintaxe:

```yaml
version: 1.4.2+48
#        │     └── BUILD NUMBER (versionCode no Android / CFBundleVersion no iOS)
#        └──────── VERSION NAME (SemVer comercial visível nas lojas)
```

- **`versionName` (`1.4.2`):** Deve seguir o padrão SemVer.
- **`buildNumber` (`48`):** Inteiro sequencial estritamente crescente. As lojas recusam uploads com build duplicado.

---

## 2. Telemetria Visual de Versão (Zero Dúvida de Cache)
Exiba obrigatoriamente a versão e o build number na tela de Login ou Configurações do app:

```dart
import 'package:package_info_plus/package_info_plus.dart';

// No rodapé da tela:
FutureBuilder<PackageInfo>(
  future: PackageInfo.fromPlatform(),
  builder: (context, snapshot) {
    if (!snapshot.hasData) return SizedBox.shrink();
    final p = snapshot.data!;
    return Text("v${p.version} (Build ${p.buildNumber}) • ${kReleaseMode ? 'PROD' : 'DEV'}",
      style: TextStyle(fontSize: 10, color: Colors.grey));
  },
);
```

---

## 3. Comandos Obrigatórios de Limpeza Profunda (Hard Reset)
Quando houver inconsistência visual ou suspeita de cache antigo:

```bash
# 1. Reset Flutter
flutter clean
flutter pub get

# 2. Reset Nativo Android (Gradle)
cd android && ./gradlew clean && cd ..

# 3. Reset Nativo iOS (Pods & DerivedData)
cd ios && rm -rf Pods Podfile.lock && pod cache clean --all && pod install --repo-update && cd ..
```

---

## 4. Injeção Automática no CI/CD
Em pipelines automatizados de build (GitHub Actions / Fastlane), passe o build dinamicamente:
```bash
flutter build appbundle --release --build-name="1.4.2" --build-number=$GITHUB_RUN_NUMBER
```
