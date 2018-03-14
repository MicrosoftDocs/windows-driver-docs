---
title: Static Driver Verifier Diagnostics
description: Static Driver Verifier Diagnostics
ms.assetid: dff22144-43a0-427f-8075-9c9152670933
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Static Driver Verifier Diagnostics


SDV has a diagnostics mode that can help you and Microsoft troubleshoot problems that SDV might encounter. When diagnostics mode is enabled, SDV logs messages to a file in your driver's sources directory, tracing SDV activity. The name of the file is StaticDVTrace.log.

### <span id="enabling_diagnostics"></span><span id="ENABLING_DIAGNOSTICS"></span>Enabling Diagnostics

To enable diagnostics mode, you must edit the Staticdv.exe.config XML configuration file that is located in the SDV bin directory. You can edit the value of the TraceLevelSwitch XML element to set the trace level to one of five values. The default value is 1 - only error messages are logged.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Level</th>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Off</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>None (default)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Error</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Only error messages</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Warning</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Warning messages and error messages</p></td>
</tr>
<tr class="even">
<td align="left"><p>Info</p></td>
<td align="left"><p>3</p></td>
<td align="left"><p>Informational messages, warning messages, and error messages</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Verbose</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>Verbose messages, informational messages, warning messages, and error messages</p></td>
</tr>
</tbody>
</table>

 

The following procedure describes how to enable diagnostic mode and how to set the level of trace activity to log.

**To enable diagnostics**

1.  Change to the %DDKPATH%\\tools\\sdv\\bin directory.

2.  Using Notepad or another text editor, open the StaticDV.exe.config file.

3.  Change the value of **DataMessagesSwitch** to **1**.
    ```
    <add name="DataMessagesSwitch" value="1" />
    ```

4.  Select a value for **TraceLevelSwitch** from **0** (no trace diagnostics) to **4** (verbose). If you are sending log files to Microsoft for diagnostics, you might be asked to set the **TraceLevelSwitch** to level **3**, which logs informational messages, warning messages, and error messages.
    ```
    <add name=" TraceLevelSwitch" value="3" />
    ```

5.  Save the StaticDV.exe.config file and run SDV on your driver.

    SDV writes the messages to the StaticDVTrace.log file in your driver's sources directory.

### <span id="the_staticdv_exe_config_file"></span><span id="THE_STATICDV_EXE_CONFIG_FILE"></span>The StaticDV.exe.config file

The following is an example configuration file that enables diagnostics and sets the tracing level to level 3 (Info).

```
<?xml version="1.0"?>
<configuration>
<system.diagnostics>
 <trace autoflush="false" indentsize="4">
 </trace>
<switches>
<!-- This switch controls data messages. In order to receive data 
         trace messages, change value="0" to value="1" -->
 <add name="DataMessagesSwitch" value="1" />
 <!-- This switch controls general messages. In order to 
         receive general trace messages change the value to the 
         appropriate level. "1" gives error messages, "2" gives errors 
         and warnings, "3" gives more detailed error information, and 
         "4" gives verbose trace information -->
  <add name="TraceLevelSwitch" value="3" />
</switches>
  </system.diagnostics>
</configuration>
```

 

 





