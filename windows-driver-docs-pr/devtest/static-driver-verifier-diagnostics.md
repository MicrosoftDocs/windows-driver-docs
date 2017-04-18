---
title: Static Driver Verifier Diagnostics
description: Static Driver Verifier Diagnostics
ms.assetid: dff22144-43a0-427f-8075-9c9152670933
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Static%20Driver%20Verifier%20Diagnostics%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




