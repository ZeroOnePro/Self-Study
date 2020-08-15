#!/bin/bash
echo "############################################"
echo "#                                          #"
echo "#                                          #"
echo "#                                          #"
echo "#                                          #"
echo "#   git add submodule auto script ver 1.0  #"
echo "#                                          #"
echo "#         written by sungminyou            #"
echo "#                                          #"
echo "#                                          #"
echo "#                                          #"
echo "############################################"
echo -e "\n"
while true; do
    read -p "Do you want rename repository? [y/n] >> " option
    if [ $option = "y" ] || [ $option = "n" ]; then
        break
    else
        echo "Invaild input please enter y or n"
        continue
    fi 
done
if [ $option == "y" ]; then
    echo -n "enter name for renaming >> "
    read name
    echo -n "enter url for add submodule >> "
    read url
    git submodule add "$url" "$name"
elif [ $option == "n" ]; then
    echo -n "enter url for add submodule >> "
    read url
    git submodule add "$url"
else
    exit 100
fi
