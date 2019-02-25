---
title: ISCSI\_ConnectionStaticInfo WMI Class
description: ISCSI\_ConnectionStaticInfo WMI Class
ms.assetid: 63af8432-3e38-451a-a26d-57b5ad1f29dd
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ISCSI\_ConnectionStaticInfo WMI Class


## <span id="ddk_iscsi_connectionstaticinfo_wmi_class_kr"></span><span id="DDK_ISCSI_CONNECTIONSTATICINFO_WMI_CLASS_KR"></span>


The ISCSI\_ConnectionStaticInfo class is used to store the static characteristics of a connection. This class is defined as follows in *Mgmt.mof*.

```cpp
class ISCSI_ConnectionStaticInfo {
  [read, WmiDataId(1), Description("A uniquely generated
    connection ID used only internally.  Do not confuse this
    with CID"): amended] 
    uint64  UniqueConnectionId;
  [read, WmiDataId(2), Description("The iSCSI connection ID
    for this connection instance."): amended] 
    uint16  CID; //session wide namespace
  [read, WmiDataId(3), 
    ISCSI_CONNECTION_STATE_TYPE_QUALIFIERS,
    Description("Indicates the current state of this
    connection"): amended, cpp_quote("\n"
    "    //login  - The TCP connection has been
           established, but a valid iSCSI\n"
    "    //login response with the final
           bit set has not been sent or received.\n"
    "    //full  - A valid iSCSI login response
           with the final bit set \n"
    "    //has been sent or received.\n"
    "    //logout  - A valid iSCSI logout command has
            been sent or received, but\n"
    "    //the TCP connection has not yet
           been closed.\n"
    "\n")] 
    ISCSI_CONNECTION_STATE_TYPE  State;
  [read, WmiDataId(4),
    ISCSI_CONNECTION_PROTOCOL_TYPE_QUALIFIERS,
    Description("The transport protocol over which this
    connection instance is running."): amended, 
    cpp_quote("\n    //The transport protocol over which
    this connection instance is running.\n")] 
    ISCSI_CONNECTION_PROTOCOL_TYPE  Protocol;
  [read, WmiDataId(5), Description("The Local Inet address
    "): amended] 
    ISCSI_IP_Address  LocalAddr;
  [read, WmiDataId(6), Description("The Local port used by
    this connection instance"): amended] 
    uint32  LocalPort;
  [read, WmiDataId(7), Description("The Remote Inet
    address"): amended] 
    ISCSI_IP_Address  RemoteAddr;
  [read, WmiDataId(8), Description("The Remote port used by
    this connection instance"): amended] 
    uint32  RemotePort;
  [read, WmiDataId(9), Description("Estimated Throughput of
    the Link"): amended] 
    uint64  EstimatedThroughput;
  [read, WmiDataId(10), Description("Maximum Datagram size
    supported by the transport"): amended] 
    uint32  MaxDatagramSize;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**ISCSI\_ConnectionStaticInfo**](https://msdn.microsoft.com/library/windows/hardware/ff561489) data structure.

 

 





