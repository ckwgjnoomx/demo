# 部署与 SSH 配置笔记

## SSH 认证
- 使用 `git@github.com:ckwgjnoomx/demo.git`
- 私钥：`C:\Users\Administrator\.ssh\id_ed25519`（ed25519，无密码短语）
- 指纹：`SHA256:sXSNENbFUPZNcdOcEVp6JMR+nKr4xDg2SZsLCKQXBeY`

## 排障要点
- Windows 自带 OpenSSH 的 `-N ""` 在 PowerShell 里可能被吞，导致私钥被误加密。
- 用 `cmd.exe /c` 或显式空参数生成无密码短语私钥更稳妥。
- git 若报 `/home/Administrator/.ssh` 路径错误，说明用了 MSYS ssh，应改用原生 `C:\Windows\System32\OpenSSH\ssh.exe`。
