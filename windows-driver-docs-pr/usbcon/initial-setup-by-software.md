---
Description: This topic describes how software enumerates a device.
title: Initial setup by software
---

# Initial setup by software


This topic describes how software enumerates a device.

For U1 or U2 transitions to occur, software performs the following steps during the enumeration of a device.

1.  Software exchanges U1 or U2 exit latency information with the device during the enumeration process. As the first part of this exchange, the device-specific latencies are filled in by the device in bU1DevExitLat and wU2DevExitLat fields of the SuperSpeed USB device capability (defined in Section 9.6.2.2 of the USB 3.0 specification). As the second part of the exchange, the host informs the device about overall exit latencies for the device by sending a SET\_SEL control transfer, as per section 9.4.12 of the USB 3.0 specification. The latency information includes the latencies that are associated with upstream links and controller.
2.  For the DS port to which the device is attached, the software configures two values: PORT\_U1\_TIMEOUT and PORT\_U2\_TIMEOUT. While deciding these values, the software takes into consideration the characteristics of the device (such as the type of endpoints) and the latencies that are associated with bringing the device back from U1 or U2 to U0. The following table describes the timeout values.

    **Table 1. PORT\_U1\_TIMEOUT and PORT\_U2\_TIMEOUT values**

    | Value   | Description                                                                                                                                                                                                                  |
    |---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | 01H-FEH | DS port must initiate transitions after a period of inactivity. The exact period is derived from the timeout value. The port must accept transitions that are initiated by the link partner unless there is pending traffic. |
    | FFH     | DS port must not initiate transitions but must accept transitions that are initiated by the link partner unless there is pending traffic.                                                                                    |
    | 0       | DS port must not initiate transitions and must not accept transitions that are initiated by the link partner.                                                                                                                |

     

3.  If the PORT\_U2\_TIMEOUT value is between 01H-FEH, there is an additional step that occurs in the hardware as a result of step 2. The DS port informs its link partner about that value. The importance of this step is described in [Direct Transition from U1 to U2](hardware-transitions.md#u1tou2) in Hardware Transitions.
4.  For every device or hub, the software configures two values: U1\_ENABLE and U2\_ENABLE by sending SET\_FEATURE (U1\_ENABLE/U2\_ENABLE) control transfers. The following table describes those values.

    **Table 2. U1\_ENABLE and U2\_ENABLE values**

    | Value    | Description                                                                                                                       |
    |----------|-----------------------------------------------------------------------------------------------------------------------------------|
    | Enabled  | US port can initiate transitions and accept transitions that are initiated by the link partner if permitted by the device policy. |
    | Disabled | US port must not initiate transitions but can accept transitions that are initiated by the link partner.                          |

     

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Initial%20setup%20by%20software%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



