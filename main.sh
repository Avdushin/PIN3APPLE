
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
          echo -e " \e[1;37m
    WWWWWWWWWWWWWWWNXXNWNNNWNXNNWWWWWWWWWWWW
    WWWWWWWWWWWWWNX0kxdxxxxkk0KNNWWWWWWWWWWW
    WWWWWWWWWWWNX0Oxdl:;;;;coxOKNWWNWWWWWWWW
    WWWWWWWWWWWN0xddoc;;::;;:lkKNWWWWWWWWWWW
    WWWWWWWWWNX0Oxoc:::;,;::;cdkKNWWWWWWWWWW
    WWWWWWWWWNXX0xo::;;;;;:c:cdOXNWWNWWWWWWW
    \e[1;34mWWWWWWWWWWWNXKxlclloddlllllxKWWNWWWWWWWW
    WWWWWWWWWWNWXkxxxkkkkkxxxkxxKWWWWWWWWWWW
    WWWWWWWWWWNKdllolllodolllooloOXWWWWWWWWW
    WWWWWWWWWWNk;;:::::lxd:;::::;oXWWWWWWWWW
    WWWWWWWWWWNOc,''',lkkko:;,,,;xXWWWWWWWWW
    WWWWWWWWWWXOxdlloxxkkkxkkddddOXWWWWWWWWW
    WWWWWWWWWWXkxxdx00OkkkO0KkoxkOXWWWWWWWWW
    \e[1;31mWWWWWWWWWWXOxko:lxkdldkxdccdx0NWWWWWWWWW
    WWWWWWWWWWWKxddodxxxddddxdodkXWWWWWWWWWW
    WWWWWWWWWWWNKOkdddxkkxdddddOXWWWWWWWWWWW
    WWWWWWWWWWWWWNXKOkkOOkkkO0XNWWWWWWWWWWWW
    WWWWWWWWWNWWWWWWWWNNNNNWWWWWWWWWWWWWWWWW
"

          echo -e "\033[0mThis program created to easy setup ANANAZZ I3 config"
          echo ""
          echo -e "\e[0;92mAuthor - https://github.com/Avdushin"
          echo -e " "
          echo -e "\e[0;91mVERSION 0.1"
          echo -e "\033[0m "
          echo  "Put""$GREEN ENTER""$NORMAL to show operation list"
          echo ""
          ;;

    # Distros

    Ubuntu)
      echo -e "\033[0;32m" 
      echo "Ubuntu script is starting..."
      echo -e "\033[0m "
      sh Ubuntu/ubuntu.sh
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

