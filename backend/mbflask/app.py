from mbflask import create_app  # パッケージ名を指定してインポート

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)