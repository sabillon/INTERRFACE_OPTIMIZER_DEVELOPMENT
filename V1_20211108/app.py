from ConfigAPI.core import app

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=5001) # Change the port to 5000 for final deployment
