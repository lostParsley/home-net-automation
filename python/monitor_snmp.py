from pysnmp.hlapi import *

def get_snmp(ip, community, oid):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community, mpModel=1),  # v2c
        UdpTransportTarget((ip, 161), timeout=1, retries=2),
        ContextData(),
        ObjectType(ObjectIdentity(oid)),
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print("SNMP error:", errorIndication)
        return None
    elif errorStatus:
        print("%s at %s" % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex)-1][0] or "?"))
        return None
    else:
        for varBind in varBinds:
            return " = ".join([x.prettyPrint() for x in varBind])

if __name__ == "__main__":
    # Example OIDs:
    # sysName.0 => 1.3.6.1.2.1.1.5.0
    # ifNumber.0 => 1.3.6.1.2.1.2.1.0
    # ifInOctets.1 => 1.3.6.1.2.1.2.2.1.10.1 (interface index 1)
    ip = "192.168.1.1"
    community = "public"
    print(get_snmp(ip, community, "1.3.6.1.2.1.1.5.0"))  # hostname
    print(get_snmp(ip, community, "1.3.6.1.2.1.2.1.0"))  # interfaces count
