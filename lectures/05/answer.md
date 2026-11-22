# 第5回 解答

## 演習

- `--list-tools` で見えたツール名と、第3回（`--mcp` なし）との違い：
  - MCP経由では `glossary_search_glossary` と `glossary_get_lecture_summary` が表示された。
  - 設定ファイルのサーバー名 `glossary` がツール名の接頭辞になり、第3回の直接登録では接頭辞なしの `search_glossary`、`get_lecture_summary` として見えていた。
- `--mcp --trace` で見えたツール呼び出し（ツール名と引数）と、`requests` の回数：
  - 質問「第2回では何を学びますか？」では `glossary_get_lecture_summary({'lecture': 2})` が呼ばれ、`requests=2`、`tool_calls=1` だった。
  - 第3回の直接登録では同じ質問に対して `get_lecture_summary({'lecture': 2})` が呼ばれ、こちらも `requests=2`、`tool_calls=1` だった。
- MCP サーバーに公開したツールと、その説明文：
  - `get_lecture_summary` を `app/mcp_server.py` の `server.tool()(tools.get_lecture_summary)` で公開した。
  - 説明文は「指定した回（1始まりの整数）の講義の要点を返す。」で、引数は `lecture`（integer）。
- fetch サーバーを足したときのツール呼び出し（ツール名と引数）：
  - 今回は fetch サーバーは追加せず、演習環境のネットワークアクセスや外部URLへの送信を行わなかった。

## 宿題

- 取り組んだレベル：発展
- やったこと：
  - `.vscode/mcp.json` に `aie-glossary` サーバーをstdio設定で追加した。
  - サーバー名は設定形式に合わせて `aie-glossary`、コマンドはリポジトリルートから `uv run python -m app.mcp_server` とした。
  - 第3回のツールと同じ関数をMCPサーバー経由でも公開できるよう、`get_lecture_summary` を追加した。
  - MCPクライアント経由のツール一覧と呼び出しを確認し、テストを追加した。
- 結果：
  - `uv run python -m app.agent --mcp --list-tools` で、MCP経由の2ツールが見えた。
  - 実測したトレースでは `glossary_get_lecture_summary({'lecture': 2})` が呼ばれ、第2回の要点を取得できた。
  - `uv run pytest -q` は13件すべて成功した。
  - Copilot ChatのAgentモードでのツール一覧、Continueによる承認、表示結果は、ユーザーがCodespacesのVS Codeから手動で確認する必要がある。
- 気づき・疑問：
  - app/agent.py は自分でMCPToolsetを組み立ててサブプロセスを起動するのに対し、Copilot Chatは`.vscode/mcp.json`の設定を読み、Agentモードでサーバーを起動してツール実行前に承認を求める設計である。
  - サーバーとツールの実装はクライアントに依存せず共通であるため、標準化されたツール情報があれば別クライアントから利用できる。
  - Chat側では、ツール実行前に人が許可するかどうか、および実行時の引数・結果がどのように表示されるかを確認して追記する。
