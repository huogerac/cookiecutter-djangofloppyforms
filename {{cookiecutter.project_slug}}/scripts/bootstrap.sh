npm install
./scripts/install_static.sh
pip install -r requirements.txt
./manage.py migrate
./manage.py

echo -e " \n\nDONE! \n\n "
echo -e " \e[32m \n\n\n\n "
echo -e "🐍 Run the comand below to start your new app:"
echo -e "./manage.py runserver\e[36m \n"
echo -e "Access the 🚀 http://localhost:8000/"
echo -e "Check the 📖 README.md out for more information \e[39m \n\n"
