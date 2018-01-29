---
title: MSiSCSI\_ManagementOperations WMI Class
description: MSiSCSI\_ManagementOperations WMI Class
ms.assetid: 1037be46-6cae-458d-8549-927c7a053195
---

# MSiSCSI\_ManagementOperations WMI Class


The MSiSCSI\_MangementOperations WMI class contains ping methods to perform ICMP ping requests to the destination addresses. This class is defined as follows in Mgmt.mof.

```
class MSiSCSI_ManagementOperations
{
    //
    // This class must be registered using PDO instance names
    //
    [key]
    string InstanceName;
 
    boolean Active;

    [WmiMethodId(10),
     Implemented,
     Description("Perform an ICMP ping") : amended,
     cpp_quote(
"//\n"
"// This method is recommended.\n"
"//\n"             
"// Ping will perform ICMP ping requests to the destination address \n"
"// and return the number of ping responses received. This is only supported\n"
"// by some HBA, use the ping command for the software initiator.\n"
"//\n"
              )            
    ]
    void PingIPAddress(
                     [in,
                      Description("Number of requests to send") : amended
                     ] uint32 RequestCount,

                     [in,
                      Description("Number of bytes in each request") : amended
                     ] uint32 RequestSize,

                     [in,
                      Description("Number of ms to wait for response") : amended
                     ] uint32 Timeout,

                     [in,
                      description("IP address to ping") : amended
                     ] ISCSI_IP_Address Address,
 
                     [out,
                      ISCSI_STATUS_QUALIFIERS
                     ] ISCSI_STATUS Status,
 
                     [out,
                      Description("Number of responses received") : amended
                     ] uint32 ResponsesReceived

                    );

 
};
```

When the WMI tool suite compiles the preceding class definition, it produces one of the [MSiSCSI\_ManagementOperations](https://msdn.microsoft.com/library/windows/hardware/ff563069) data structures.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_ManagementOperations%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




