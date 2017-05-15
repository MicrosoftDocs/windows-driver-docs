---
title: GPIO Extensions
description: The General Purpose Input/Output (GPIO) extension commands display the software state of GPIO controllers.
ms.assetid: 1703C402-D770-4D3F-AB70-F2D30712A5D9
---

# GPIO Extensions


The General Purpose Input/Output (GPIO) extension commands display the software state of GPIO controllers. These commands display information from data structures maintained by the GPIO framework extension driver (Msgpioclx.sys). For information about the GPIO framework extension, see [General-Purpose I/O (GPIO) Drivers](http://go.microsoft.com/fwlink/p?LinkID=299823).

The GPIO debugger extension commands are implemented in gpiokd.dll. To load the GPIO commands, enter **.load gpiokd.dll** in the debugger.

Each GPIO controller has a set of banks. Each bank has a pin table that has an array of pins. The GPIO debugger extension commands display information about GPIO controllers, banks, pin tables, and pins.

## <span id="data_structures_used_by_the_gpio_commands"></span><span id="DATA_STRUCTURES_USED_BY_THE_GPIO_COMMANDS"></span>Data structures used by the GPIO commands


The GPIO debugger extension commands use these data structures, which are defined by Msgpioclx.sys.

<span id="msgpioclx__DEVICE_EXTENSION"></span><span id="msgpioclx__device_extension"></span><span id="MSGPIOCLX__DEVICE_EXTENSION"></span>**msgpioclx!\_DEVICE\_EXTENSION**  
The device extension structure for the GPIO framework extension driver. This structure holds information about an individual GPIO controller.

<span id="msgpioclx__GPIO_BANK_ENTRY"></span><span id="msgpioclx__gpio_bank_entry"></span><span id="MSGPIOCLX__GPIO_BANK_ENTRY"></span>**msgpioclx!\_GPIO\_BANK\_ENTRY**  
This structure holds information about an individual bank of a GPIO controller.

<span id="msgpioclx__GPIO_PIN_INFORMATION_ENTRY"></span><span id="msgpioclx__gpio_pin_information_entry"></span><span id="MSGPIOCLX__GPIO_PIN_INFORMATION_ENTRY"></span>**msgpioclx!\_GPIO\_PIN\_INFORMATION\_ENTRY**  
This structure holds information about an individual pin in a bank of a GPIO controller.

## <span id="Getting_started_with_GPIO_debugging"></span><span id="getting_started_with_gpio_debugging"></span><span id="GETTING_STARTED_WITH_GPIO_DEBUGGING"></span>Getting started with GPIO debugging


To start debugging a GPIO issue, enter the [**!gpiokd.clientlist**](-gpiokd-clientlist.md) command. The **!gpiokd.clientlist** command displays an overview of all registered GPIO controllers and displays addresses that you can pass to other GPIO debugger commands.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>!gpiokd.help</strong>](-gpiokd-help.md)</p></td>
<td align="left"><p>The [<strong>!gpiokd.help</strong>](-gpiokd-help.md) command displays help for the GPIO debugger extension commands.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!gpiokd.bankinfo</strong>](-gpiokd-bankinfo.md)</p></td>
<td align="left"><p>The [<strong>!gpiokd.bankinfo</strong>](-gpiokd-bankinfo.md) command displays information about a GPIO bank.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!gpiokd.clientlist</strong>](-gpiokd-clientlist.md)</p></td>
<td align="left"><p>The [<strong>!gpiokd.clientlist</strong>](-gpiokd-clientlist.md) command displays all registered GPIO controllers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!gpiokd.gpioext</strong>](-gpiokd-gpioext.md)</p></td>
<td align="left"><p>The [<strong>!gpiokd.gpioext</strong>](-gpiokd-gpioext.md) command displays information about a GPIO controller.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!gpiokd.pininfo</strong>](-gpiokd-pininfo.md)</p></td>
<td align="left"><p>The [<strong>!gpiokd.pininfo</strong>](-gpiokd-pininfo.md) command displays information about a specified GPIO pin.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!gpiokd.pinisrvec</strong>](-gpiokd-pinisrvec.md)</p></td>
<td align="left"><p>The [<strong>!gpiokd.pinisrvec</strong>](-gpiokd-pinisrvec.md) command displays Interrupt Service Routine (ISR) vector information for a specified pin.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!gpiokd.pintable</strong>](-gpiokd-pintable.md)</p></td>
<td align="left"><p>The [<strong>!gpiokd.pintable</strong>](-gpiokd-pintable.md) command displays information about an array of GPIO pins.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Specialized Extension Commands](specialized-extensions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20GPIO%20Extensions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





