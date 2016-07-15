---
Description: 'This topic discusses how the Windows port class driver (PortCls) can use a new Windows 8 interface to manipulate the exit latency requirement for the D3 sleep state.'
MS-HAID: 'audio.portcls\_d3\_exit\_latency\_requirement'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: PortCls D3 Exit Latency Requirement
---

# PortCls D3 Exit Latency Requirement


This topic discusses how the Windows port class driver (PortCls) can use a new Windows 8 interface to manipulate the exit latency requirement for the D3 sleep state.

When a system enters a platform power state other than fully working (for example, sleep or connected standby), the required exit latency for the audio adapter to return to D0 (fully working) can be relaxed. This makes it possible for the audio adapter to use sleep states deeper than D3, even if these deeper states could result in longer exit latencies (exit times).

PortCls can now use a new power management interface to generate a new D3 exit latency tolerance, and then communicate it dynamically to the audio miniport driver. These tolerances are represented as [**PC\_EXIT\_LATENCY**](audio.pc_exit_latency) enumeration values.

For more information about the new power management interface, see [**IAdapterPowerManagement3**](audio.iadapterpowermanagement3)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20PortCls%20D3%20Exit%20Latency%20Requirement%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


