# ! /bin/bash

# input pacs ip
echo " ----------------- please enter pacs ip address --------------------- "
read -p "Pacs ip address: " pacs_ip
if [ -z "$pacs_ip" ]; then
    echo "ERROR:pacs ip address cannot be empty..."
    exit 1;
fi

# input pacs aet
echo " --------------------- please enter pacs aet ------------------------ "
read -p "pacs aet: " pacs_aet
if [ -z "$pacs_aet" ]; then
    echo "ERROR:pacs aet cannot be empty..."
    exit 1;
fi

# input pacs port
echo " -------------------  please enter pacs port  ----------------------- "
read -p "pacs port: " pacs_port
if [ -z "$pacs_port" ]; then
    echo "ERROR:pacs port cannot be empty..."
    exit 1;
fi

temp=$(grep H0sp1tal /home/biomind/.biomind/var/biomind/orthanc/orthanc.json)

# create H0sp1tal 
if [ -z "$temp" ]; then
    echo "There is no H0sp1tal, creating and adding..."
    sed -i "/DicomModalities/{s/.*/\"DicomModalities\": \{\n        \"H0sp1tal\": \{\n            \"AET\": \"${pacs_aet}\",\n            \"Host\": \"${pacs_ip}\",\n            \"Port\": ${pacs_port},\n            \"AllowEcho\": true,\n            \"AllowFind\": true,\n            \"AllowMove\": true,\n            \"AllowStore\": true\n        \},/}" /home/biomind/.biomind/var/biomind/orthanc/orthanc.json

# modify H0sp1tal
else
    echo "H0sp1tal is already exist, only changing..."
    sed -i "/H0sp1tal/{N;N;N;s/.*/        \"H0sp1tal\": \{\n            \"AET\": \"${pacs_aet}\",\n            \"Host\": \"${pacs_ip}\",\n            \"Port\": ${pacs_port},/}" /home/biomind/.biomind/var/biomind/orthanc/orthanc.json
fi





