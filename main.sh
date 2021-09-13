
# variables
GREEN=$'\033[0;32m'
NORMAL=$'\033[0m'

clear
sh welcome.sh
echo "Author - https://github.com/Avdushin"
echo ""
echo "Choose your distro..."
echo " "


# sudo cp -r polybar/ ~/.config/ && sudo cp -r /walls/ ~/ && sudo tar -xf sublime_text_build_4113_x64.tar.xz  -C ~/.appz 

select opt in Distro_info Ubuntu Manjaro Fedora Solus Neofetch About quit ; do

    PS3="Select the operation: "

  case $opt in

        Distro_info)
          echo "Info about your system "
          lsb_release -a
          echo ""
          echo  "Put""$GREEN ENTER""$NORMAL to show operation list"
          echo ""
          ;;
        About) 
          clear
          echo -e " \e[0;1;33m
                                                           
______ _____ _   _ _____  ___ ____________ _     _____ 
| ___ |_   _| \ | |____ |/ _ \| ___ | ___ | |   |  ___|
| |_/ / | | |  \| |   / / /_\ | |_/ | |_/ | |   | |__  
|  __/  | | | .   |   \ |  _  |  __/|  __/| |   |  __| 
| |    _| |_| |\  .___/ | | | | |   | |   | |___| |___ 
\_|    \___/\_| \_\____/\_| |_\_|   \_|   \_____\____/ 
                                                       
\033[0m  
 "

          echo "This program created to easy setup ANANAZZ I3 config"
          echo ""
          echo -e "\e[0;92mAuthor - https://github.com/Avdushin"
          echo -e " "
          echo -e "\e[0;91mVERSION 0.0"
          echo -e "\033[0m "
          echo  "Put""$GREEN ENTER""$NORMAL to show operation list"
          echo ""
          ;;

    # Distros

    Ubuntu)
      echo ""
      echo "Ubuntu script is starting..."
      cat Ubuntu/ubuntu.sh
      sudo cp Themes/Solarized-Dark-Cyan-GS-3.36/ /usr/share/themes/
      echo ""
      break
      ;;
    Manjaro)
      echo ""
      echo "Manjaro script is starting..."
      echo ""
      sh Manjaro/manjaro.sh
      sudo cp Themes/Solarized-Dark-Cyan-GS-3.36/ /usr/share/themes/
      echo ""
      exit
      break
      ;;
    Fedora)
      echo ""
      echo "Fedora script is starting..."
      echo ""
      sh Fedora/fedora.sh
      sudo cp Themes/Solarized-Dark-Cyan-GS-3.36/ /usr/share/themes/
      echo ""
      break
      ;;
    Solus)
      echo ""
      echo "solus script is starting..."
      echo ""
      sh Solus/solus.sh
      echo ""
      break
      ;;
    Neofetch)
      neofetch
      echo  "Put""$GREEN ENTER""$NORMAL to show operation list" 
      echo -e "$NORMAL"
      ;;
    quit)
      break
      ;;
    *) 
      echo "Invalid option $REPLY"
      ;;
  esac
done

