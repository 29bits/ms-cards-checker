if [ "$1" = "--help" ];
then
  docker run cards-checker --help
elif [ "$1" = "" ]
then
    docker run cards-checker --help
elif [ -f "$1" ]
then
  absolutePath="$(readlink -f $1)"
  fileName="$(basename -- $absolutePath)"
  docker run --volume "$absolutePath":/usr/src/app/"$fileName" cards-checker "$fileName"
else
  echo "ERROR: Provided file $1 does not exist"
fi