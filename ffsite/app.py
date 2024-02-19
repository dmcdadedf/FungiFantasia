from ffsite import create_app


app = create_app()


if __name__ == "__main__":
    print("RUN APP")
    app.run(
        debug=False,
        host='0.0.0.0',
        port=8080
    )