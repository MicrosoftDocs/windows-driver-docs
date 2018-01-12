---
title: ISCSI\_ConnectionStaticInfo WMI Class
description: ISCSI\_ConnectionStaticInfo WMI Class
ms.assetid: 63af8432-3e38-451a-a26d-57b5ad1f29dd
---

# ISCSI\_ConnectionStaticInfo WMI Class


## <span id="ddk_iscsi_connectionstaticinfo_wmi_class_kr"></span><span id="DDK_ISCSI_CONNECTIONSTATICINFO_WMI_CLASS_KR"></span>


The ISCSI\_ConnectionStaticInfo class is used to store the static characteristics of a connection. This class is defined as follows in *Mgmt.mof*.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ISCSI_ConnectionStaticInfo%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




