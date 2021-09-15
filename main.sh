
# variables
GREEN=$'\033[0;32m'
NORMAL=$'\033[0m'

sh welcome.sh
echo -e "\e[0;92mAuthor - https://github.com/Avdushin"
echo ""
echo -e "\e[0;1;33mChoose your distro..." 
echo -e "\033[0m "

select opt in Ubuntu Fedora Manjaro Solus Distro_info Neofetch About quit ; do

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
      echo -e "\033[0;32m" 
      echo "Ubuntu script is starting..."
      echo -e "\033[0m "
      cat Ubuntu/ubuntu.sh
      echo ""
      break
      ;;
   Manjaro)
      echo -e "\033[0;32m" 
      echo "Manjaro script is starting..."
      echo -e "\033[0m "
      sh Manjaro/manjaro.sh
      echo ""
      exit
      break
      ;;
    Fedora)
      echo -e "\033[0;32m" 
      echo "Fedora script is starting..."
      echo -e "\033[0m "
      echo ""
      sh Fedora/fedora.sh
      echo ""
      break
      ;;
    Solus)
      echo -e "\033[0;32m" 
      echo "solus script is starting..."
      echo -e "\033[0m "
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
      echo -e "\e[0;91mInvalid option $REPLY"
      echo -e "\033[0m "
      ;;
  esac
done

