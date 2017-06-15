---
title: Determining Whether the Operating System Is Running in Safe Mode
author: windows-driver-content
description: Determining Whether the Operating System Is Running in Safe Mode
MS-HAID:
- 'Other\_21c75869-2e21-4b39-958f-64904e504ca8.xml'
- 'kernel.determining\_whether\_the\_operating\_system\_is\_running\_in\_safe\_mode'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5724a731-81a2-4c4e-a9e2-146859977e44
keywords: ["Safe Mode WDK kernel", "operating system Safe Mode WDK kernel", "InitSafeBootMode", "preventing Safe Mode WDK kernel", "checking Safe Mode", "verifying Safe Mode", "startup Safe Mode WDK kernel"]
---

# Determining Whether the Operating System Is Running in Safe Mode


This topic describes how a device driver can determine whether the operating system that it is running on was started in Safe Mode. This topic also describes how to prevent a driver from operating in Safe Mode.

The Microsoft Windows operating system kernel exports a pointer named **InitSafeBootMode**. **InitSafeBootMode** points to a ULONG variable that contains the Safe Mode settings that are currently in effect. A device driver can examine these settings to determine whether the operating system is running in Safe Mode.

The following table lists the modes for values of the **InitSafeBootMode** variable.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Mode</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>The operating system is not in Safe Mode.</p></td>
</tr>
<tr class="even">
<td><p>1</p></td>
<td><p>SAFEBOOT_MINIMAL</p></td>
</tr>
<tr class="odd">
<td><p>2</p></td>
<td><p>SAFEBOOT_NETWORK</p></td>
</tr>
<tr class="even">
<td><p>3*</p></td>
<td><p>SAFEBOOT_DSREPAIR</p></td>
</tr>
</tbody>
</table>

 

**Note**  \* The value 3 applies to Windows domain controllers only.

 

To use the **InitSafeBootMode** variable, you must declare it in your driver, as the following code example shows.

```
extern PULONG InitSafeBootMode;
```

After you declare **InitSafeBootMode**, you can use the following code example to determine whether the operating system is running in Safe Mode.

```
if (*InitSafeBootMode > 0) {
    // The operating system is in Safe Mode.
    // Take appropriate action.
    //
}
```

To prevent a driver from operating in Safe Mode, use the technique in the following list that matches your driver type:

-   **Function drivers**

    If your function driver has a service start type of SERVICE\_BOOT\_START, check the value of **InitSafeBootMode** in the function driver's *AddDevice* routine. If the system is in Safe Mode, return a failure status.

    **Note**   You must never return failure from the **DriverEntry** routine.

     

-   **Filter drivers**

    If your filter driver starts during system startup, check the value of **InitSafeBootMode** in the filter driver's *AddDevice* routine. If the operating system is in Safe Mode, do the following:

    1.  Do not attach the filter device object to the device stack.
    2.  Return success from the filter driver's *AddDevice* routine.
-   **Other drivers**

    For drivers other than function or filter drivers, check the value of **InitSafeBootMode** in the driver's **DriverEntry** routine. If the operating system is in Safe Mode, return a failure status.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Determining%20Whether%20the%20Operating%20System%20Is%20Running%20in%20Safe%20Mode%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


