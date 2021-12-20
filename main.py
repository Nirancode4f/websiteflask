from website import  create_app

app = create_app()

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0',port=8080)