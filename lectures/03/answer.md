# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
- `--trace` で見えたツール呼び出し（ツール名と引数）：
- 1つの質問での LLM 呼び出し回数（`requests`）：
- 追加したツールと、docstring に書いた説明：

## 宿題

- 取り組んだレベル：発展(a)
- やったこと：Pydantic AI 版と同じ `INSTRUCTIONS`、`search_glossary`、`get_lecture_summary` を使う Google ADK 版を `adk_app/` に作りました。`GOOGLE_API_KEY` が未設定で `GEMINI_API_KEY` が設定されている場合は、既存の講座環境でも動くように ADK 用の環境変数へ引き継ぐようにしました。
- 実行方法：Codespaces のポート転送から開く場合は `uv run adk web --no-reload --host 0.0.0.0 --allow_origins '*' --port 8000 adk_app` で起動し、転送されたポートの URL をブラウザで開く。エージェントの一覧から `adk_app` を選び、「LoRAとは？」「第3回では何を学ぶ？」を入力する。
- 結果：`--allow_origins '*'` を付けると UI の HTML と JavaScript が `200 OK` で取得でき、403 は解消した。ブラウザから `adk_app` の検出、セッション作成、質問の送信まで確認できたが、今回の環境の `GEMINI_API_KEY` は Google API から `API_KEY_INVALID` と判定され、回答表示は確認できなかった。API キーなしで実行できる既存のテスト12件と、ADK 版のツール登録テストは通った。
- 比較：Pydantic AI 版は `Agent` に関数を登録して `run_sync` する構成で、CLI の `--trace` からツール呼び出しを確認する。ADK 版は `root_agent` を公開する構成で、`adk web` が実行ループ、セッション履歴、ツール呼び出しの表示をまとめて提供する。ADK は Web UI ですぐ試せる一方、既存の CLI のような細かな出力形式は自分で作る必要がある。
- 気づき・疑問：どちらも Python 関数をツールとして登録できるが、エージェントを発見して UI から実行するための規約は ADK の方が強い。学習用途では、会話履歴とツール実行の様子をブラウザで確認できる点が便利だった。
