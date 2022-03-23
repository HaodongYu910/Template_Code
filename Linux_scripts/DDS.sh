## This is DDS auto-testing shell script code

echo ""
echo " ==================================================================== "
echo "              welcome to use auto-installing of DDS                   "
echo "                                            @copyright by HaodongYU   "
echo " ==================================================================== "
echo ""

# stop old dicommaster
dicommaster stop

# input local ip
echo " ----------------- please enter local ip address --------------------- "
read -p "Local ip address: " local_ip
if [ -z "$local_ip" ]; then
    echo "ERROR:local ip address cannot be empty..."
    exit 1;
fi

# input dds package name
echo " ----------------- please enter DDS package name --------------------- "
read -p "DDS installing package name: " DDS_pck
if [ -z "$DDS_pck" ]; then
    echo "ERROR: DDS installing package name cannot be empty..."
    exit 1;
fi

# input dds version
echo " -----------------   please enter DDS version   --------------------- "
read -p "DDS version: " DDS_version
if [ -z "$DDS_version" ]; then
    echo "ERROR: DDS version cannot be empty..."
    exit 1;
fi

# input query tool
echo " -----------------    please enter query tool    -------------------- "
read -p "query tool (DB,PYNETDICOM?): " query_tool
if [ -z "$query_tool" ]; then
    echo "you must choose a query tool..."
    exit 1;
fi



## installing
echo ""
echo " ==================================================================== "
echo "                        Starting install              "
echo " ==================================================================== "
echo ""

# change home address of DDS
cd /home/biomind/DicomMaster
unzip $DDS_pck.zip
cd /home/biomind/DicomMaster/$DDS_pck/DicomMaster/
sh scripts/dicommaster.sh install ../dicommaster\:$DDS_version.tar


echo ""
echo " >>>>>>>>>>>>>>>>>>>>> Homepath setup complete <<<<<<<<<<<<<<<<<<<<<<< "
echo ""

## modify config.yml
echo ""
echo " ==================================================================== "
echo "                   Starting modify aet configure                 "
echo " ==================================================================== "
echo ""
cd ~/DicomMaster/$DDS_pck/DicomMaster/dicommaster/sync_pacs/config

# grab local aet
#   awk command get the value of second column which satisfy "DicomAet" 
#   cut command use " as a split character and get the value of second field
local_aet=$(awk '/DicomAet/{print$2}' /home/biomind/.biomind/var/biomind/orthanc/orthanc.json | cut -d \" -f 2)
# grab local port
local_port=$(awk '/DicomPort/{print$2}' /home/biomind/.biomind/var/biomind/orthanc/orthanc.json | cut -d , -f 1)
# grap hospital aet
hsp_aet=$(awk -v hspaet_line=$(awk '/H0sp1tal/{print NR}' /home/biomind/.biomind/var/biomind/orthanc/orthanc.json) '{if(NR==hspaet_line+1){print $0}}' /home/biomind/.biomind/var/biomind/orthanc/orthanc.json | cut -d \" -f 4)
# grap hospital ip
hsp_ip=$(awk -v hspip_line=$(awk '/H0sp1tal/{print NR}' /home/biomind/.biomind/var/biomind/orthanc/orthanc.json) '{if(NR==hspip_line+2){print $0}}' /home/biomind/.biomind/var/biomind/orthanc/orthanc.json | cut -d \" -f 4)
#grap hospital port
hsp_port=$(awk -v hspport_line=$(awk '/H0sp1tal/{print NR}' /home/biomind/.biomind/var/biomind/orthanc/orthanc.json) '{if(NR==hspport_line+3){print $0}}' /home/biomind/.biomind/var/biomind/orthanc/orthanc.json | cut -d : -f 2 | cut -d , -f 1)


# 如果要替换的内容中存在单引号，需要把指令行中的单引号替换成双引号即可。 
sed -i "/query_tool:/{N;N;s/.*/  query_tool:\n    type: 'text'\n    value: '$query_tool'        # PYNETDICOM, GRAPHQL, DB/}" config.yaml

# called_aet
sed -i "/called_aet:/{N;N;s/.*/  called_aet:\n    type: 'text'\n    value: '${hsp_aet}'/}" config.yaml
# called_ip
sed -i "/called_ip:/{N;N;s/.*/  called_ip:\n    type: 'text'\n    value: '${hsp_ip}'/}" config.yaml
# called_port
sed -i "/called_port:/{N;N;s/.*/  called_port:\n    type: 'text'\n    value: ${hsp_port}/}" config.yaml

# local_aet
sed -i "/local_aet:/{N;N;s/.*/  local_aet:\n    type: 'text'\n    value: '${local_aet}'/}" config.yaml
# local_ip
sed -i "/local_ip:/{N;N;s/.*/  local_ip:\n    type: 'text'\n    value: '${local_ip}'/}" config.yaml

# movedest_aet
sed -i "/movedest_aet:/{N;N;s/.*/  movedest_aet:\n    type: 'text'\n    value: '${local_aet}'/}" config.yaml
# movedest_ip
sed -i "/movedest_ip:/{N;N;s/.*/  movedest_ip:\n    type: 'text'\n    value: '${local_ip}'/}" config.yaml
# movedest_port
sed -i "/movedest_port:/{N;N;s/.*/  movedest_port:\n    type: 'text'\n    value: ${local_port}/}" config.yaml

if [ "$query_tool" == "DB" ]; then
    echo ""
    echo " ==================================================================== "
    echo "                   Starting modify DB configure                       "
    echo " ==================================================================== "
    echo ""
    # pacs_dbaddr
    sed -i "/pacs_dbaddr:/{N;N;s/.*/  pacs_dbaddr:\n    type: 'text'\n    value: '192.168.1.228'/}" config.yaml
    # pacs_dbname
    sed -i "/pacs_dbname:/{N;N;s/.*/  pacs_dbname:\n    type: 'text'\n    value: 'miPlatform'/}" config.yaml
    # pacs_username
    sed -i "/pacs_username:/{N;N;s/.*/  pacs_username:\n    type: 'text'\n    value: 'yuhaodong'/}" config.yaml
    # pacs_password
    sed -i "/pacs_password:/{N;N;s/.*/  pacs_password:\n    type: 'text'\n    value: '123123'/}" config.yaml
    # pacs_port
    sed -i "/pacs_port:/{N;N;s/.*/  pacs_dbname:\n    type: 'text'\n    value: '1433'/}" config.yaml
    # pacs_sqlquery 
    sed -i "/pacs_sqlquery:/{N;N;s/.*/  pacs_sqlquery:\n    type: 'text'\n    value: \"select StudyInstanceUID from V_Study where Modalities in ('CT', 'MR')\"/}" config.yaml
    
    echo ""
    echo " >>>>>>>>>>>>>>>>>  DB configure modified complete <<<<<<<<<<<<<<<<<<<< "
    echo ""
else
    echo ""
    echo " ==================================================================== "
    echo "                   You choose to use PYNETDICOM                       "
    echo " ==================================================================== "
    echo ""

fi

echo ""
echo " >>>>>>>>>>>>>>>>>>>>>>>  Starting dicommaster <<<<<<<<<<<<<<<<<<<<<<<< "
echo ""
dicommaster start
echo ""
echo " >>>>>>>>>>>>>>>>>>>  Auto installation complete <<<<<<<<<<<<<<<<<<<<<< "
echo ""



