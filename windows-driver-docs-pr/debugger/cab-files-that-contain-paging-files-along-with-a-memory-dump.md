---
title: CAB Files that Contain Paging Files Along with a Memory Dump
description: A memory dump file can be placed in a cabinet (CAB) file along with paging files.
ms.assetid: 89B54522-1B21-4E4E-9AF3-1F637E3BA50F
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CAB Files that Contain Paging Files Along with a Memory Dump


A memory dump file can be placed in a cabinet (CAB) file along with paging files. When a Windows debugger analyzes the memory dump file, it can use the paging files to present a full view memory, including memory that was paged out when the dump file was created.

Suppose a CAB file named MyCab.cab contains these files:

Memory.dmp
Cabmanifest.xml
Pagefile.sys
Also suppose Cabmanifest.xml looks like this:

```XML
<?xml version="1.0" encoding="UTF-8"?>
<WatsonPageFileManifest>
  <Pagefiles>
    <Pagefile Name="pagefile.sys"></Pagefile>
  </Pagefiles>
</WatsonPageFileManifest>
```

You can open the CAB file by entering one of these commands:

-   **windbg /z MyCab.cab**
-   **kd /z MyCab.cab**

The debugger reads Cabmanifest.xml for a list of paging files that are to be included in the debugging session. In this example, there is only one paging file. The debugger converts the paging file to a Target Information File (TIF) file that it can use during the debugging session. Because the debugger has access to the TIF, it can display memory that was paged out at the time the dump file was created.

Regardless of how many paging files are in the CAB file, the debugger uses only the paging files that are listed in Cabmanifest.xml. Here's an example of a CAB manifest file that lists three paging files.

```XML
<?xml version="1.0" encoding="UTF-8"?>
<WatsonPageFileManifest>
  <Pagefiles>
    <Pagefile Name="pagefile1.sys"></Pagefile>
    <Pagefile Name="pagefile2.sys"></Pagefile>
    <Pagefile Name="swapfile.sys"></Pagefile>
  </Pagefiles>
</WatsonPageFileManifest>
```

In Cabmanifest.xml, the paging files must be listed in the same order that Windows uses them. That is, they must be listed in the order that they appear in the Registry.

The memory dump file that you put in the CAB file must be a complete memory dump. You can use Control Panel to configure Windows to create a complete memory dump when there is a crash. For example, in Windows 8 you can go to **Control Panel &gt; System and Security &gt; System &gt; Advanced System Settings &gt; Startup and Recovery**. As an alternative to using Control Panel, you can set the value of this registry entry to 1.

**HKLM**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**CrashControl**\\**CrashDumpEnabled**

Starting in Windows 8.1, you can configure Windows to preserve the contents of paging files when Windows restarts.

To specify that you want paging files to be saved when Windows restarts, set the value of this registry entry to 1.

**HKLM**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**CrashControl**\\**SavePageFileContents**

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20CAB%20Files%20that%20Contain%20Paging%20Files%20Along%20with%20a%20Memory%20Dump%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




