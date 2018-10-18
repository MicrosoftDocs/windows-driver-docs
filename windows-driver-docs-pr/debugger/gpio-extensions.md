---
title: GPIO Extensions
description: The General Purpose Input/Output (GPIO) extension commands display the software state of GPIO controllers.
ms.assetid: 1703C402-D770-4D3F-AB70-F2D30712A5D9
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# GPIO Extensions


The General Purpose Input/Output (GPIO) extension commands display the software state of GPIO controllers. These commands display information from data structures maintained by the GPIO framework extension driver (Msgpioclx.sys). For information about the GPIO framework extension, see [General-Purpose I/O (GPIO) Drivers](http://go.microsoft.com/fwlink/p?LinkID=299823).

The GPIO debugger extension commands are implemented in gpiokd.dll. To load the GPIO commands, enter **.load gpiokd.dll** in the debugger.

Each GPIO controller has a set of banks. Each bank has a pin table that has an array of pins. The GPIO debugger extension commands display information about GPIO controllers, banks, pin tables, and pins.

## <span id="data-structures-used-by-the-gpio-commands"></span><span id="DATA_STRUCTURES_USED_BY_THE_GPIO_COMMANDS"></span>Data structures used by the GPIO commands


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
<td align="left"><p><strong>[!gpiokd.help](-gpiokd-help.md)</strong></p></td>
<td align="left"><p>The <strong>[!gpiokd.help](-gpiokd-help.md)</strong> command displays help for the GPIO debugger extension commands.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[!gpiokd.bankinfo](-gpiokd-bankinfo.md)</strong></p></td>
<td align="left"><p>The <strong>[!gpiokd.bankinfo](-gpiokd-bankinfo.md)</strong> command displays information about a GPIO bank.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[!gpiokd.clientlist](-gpiokd-clientlist.md)</strong></p></td>
<td align="left"><p>The <strong>[!gpiokd.clientlist](-gpiokd-clientlist.md)</strong> command displays all registered GPIO controllers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[!gpiokd.gpioext](-gpiokd-gpioext.md)</strong></p></td>
<td align="left"><p>The <strong>[!gpiokd.gpioext](-gpiokd-gpioext.md)</strong> command displays information about a GPIO controller.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[!gpiokd.pininfo](-gpiokd-pininfo.md)</strong></p></td>
<td align="left"><p>The <strong>[!gpiokd.pininfo](-gpiokd-pininfo.md)</strong> command displays information about a specified GPIO pin.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[!gpiokd.pinisrvec](-gpiokd-pinisrvec.md)</strong></p></td>
<td align="left"><p>The <strong>[!gpiokd.pinisrvec](-gpiokd-pinisrvec.md)</strong> command displays Interrupt Service Routine (ISR) vector information for a specified pin.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[!gpiokd.pintable](-gpiokd-pintable.md)</strong></p></td>
<td align="left"><p>The <strong>[!gpiokd.pintable](-gpiokd-pintable.md)</strong> command displays information about an array of GPIO pins.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Specialized Extension Commands](specialized-extensions.md)

 

 






