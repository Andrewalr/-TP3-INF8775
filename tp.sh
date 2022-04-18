
while getopts "e:p" flag
do
    case "${flag}" in
        e) path=${OPTARG};;
        p) sol="true";;

    esac
done

#ALGO GLOUTON

if [ "$sol" == 'true' ]
then
    python3 algo.py $path $sol

else
    python3 algo.py $path false
fi
