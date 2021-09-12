
# variables
GREEN=$'\033[0;32m'
NORMAL=$'\033[0m'

echo " 
 _    _ _____ _     _____ ________  ________   _____ _____ 
| |  | |  ___| |   /  __ |  _  |  \/  |  ___| |_   _|  _  |
| |  | | |__ | |   | /  \| | | | .  . | |__     | | | | | |
| |/\| |  __|| |   | |   | | | | |\/| |  __|    | | | | | |
\  /\  | |___| |___| \__/\ \_/ | |  | | |___    | | \ \_/ /
 \/  \/\____/\_____/\____/\___/\_|  |_\____/    \_/  \___/ 
                                                           
                                                           
______ _____ _   _ _____  ___ ____________ _     _____ 
| ___ |_   _| \ | |____ |/ _ \| ___ | ___ | |   |  ___|
| |_/ / | | |  \| |   / / /_\ | |_/ | |_/ | |   | |__  
|  __/  | | | .   |   \ |  _  |  __/|  __/| |   |  __| 
| |    _| |_| |\  .___/ | | | | |   | |   | |___| |___ 
\_|    \___/\_| \_\____/\_| |_\_|   \_|   \_____\____/ 
                                                       
                                                       
 "

echo "Author - https://github.com/Avdushin"
echo ""
echo "Choose your distro..."
echo " "


# sudo cp -r polybar/ ~/.config/ && sudo cp -r /walls/ ~/ && sudo tar -xf sublime_text_build_4113_x64.tar.xz  -C ~/.appz 

select opt in Distro_info Ubuntu Manjaro Solus Neofetch About quit ; do

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
          echo " 
 _    _ _____ _     _____ ________  ________   _____ _____ 
| |  | |  ___| |   /  __ |  _  |  \/  |  ___| |_   _|  _  |
| |  | | |__ | |   | /  \| | | | .  . | |__     | | | | | |
| |/\| |  __|| |   | |   | | | | |\/| |  __|    | | | | | |
\  /\  | |___| |___| \__/\ \_/ | |  | | |___    | | \ \_/ /
 \/  \/\____/\_____/\____/\___/\_|  |_\____/    \_/  \___/ 
                                                           
                                                           
______ _____ _   _ _____  ___ ____________ _     _____ 
| ___ |_   _| \ | |____ |/ _ \| ___ | ___ | |   |  ___|
| |_/ / | | |  \| |   / / /_\ | |_/ | |_/ | |   | |__  
|  __/  | | | .   |   \ |  _  |  __/|  __/| |   |  __| 
| |    _| |_| |\  .___/ | | | | |   | |   | |___| |___ 
\_|    \___/\_| \_\____/\_| |_\_|   \_|   \_____\____/ 
                                                       

 "
          echo "This program created to easy setup ANANAZZ I3 config"
          echo "Author - https://github.com/Avdushin"
          echo ""
          echo "VERSION 0.0"
          echo ""
          echo ""
          ;;

    # Distros

    Ubuntu)
      chmod +x lol.sh 
      echo "Ubuntu script is starting..."
      sh lol.sh
      echo ""
      break
      ;;
    Manjaro)
      chmod +x lol.sh 
      echo "Manjaro script is starting..."
      sh lol.sh
      echo ""
      break
      ;;
    Solus)
      chmod +x lol.sh 
      echo "solus script is starting..."
      sh lol.sh
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

