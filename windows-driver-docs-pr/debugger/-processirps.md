---
title: processirps
description: The processirps extension displays information about I/O request packets (IRPs) associated with processes.
ms.assetid: B7CC72A5-7D3F-4DE5-878D-ABD08BAF227C
keywords: ["processirps Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- processirps
api_type:
- NA
---

# !processirps


The **!processirps** extension displays information about I/O request packets (IRPs) associated with processes.

```
!processirps
!processirps ProcessAddress [Flags]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_ProcessAddress"></span><span id="_processaddress"></span><span id="_PROCESSADDRESS"></span> **** *ProcessAddress*  
The address of a process. If you specify *ProcessAddress*, only IRPs associated with that process are displayed. If you do not specify *ProcessAddress*, IRPs for all processes are displayed.

<span id="_Flags"></span><span id="_flags"></span><span id="_FLAGS"></span> **** *Flags*  
A bitwise OR of one or more of the following flags.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Display IRPs queued to threads.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Display IRPs queued to file objects.

If you specify *Flags*, you must also specify *ProcessAddress*. If you do not specify *Flags*, IRPs queued to both threads and file objects are displayed.

## <span id="ddk__processfields_dbg"></span><span id="DDK__PROCESSFIELDS_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

kdexts.dll

Remarks
-------

This command enables you to quickly identify any queued IRPs for a process, both those that are queued to threads and those that are queued to file objects. IRPs are queued to a file object when the file object has a completion port associated with it.

Examples
--------

You can use [**!process**](-process.md) command to get process addresses. For example, you could get the process address for explorer.exe.

```
2: kd> !process 0 0
**** NT ACTIVE PROCESS DUMP ****
...
PROCESS fffffa800688c940
    SessionId: 1  Cid: 0bbc    Peb: 7f70da5e000  ParentCid: 0b84
    DirBase: 2db10000  ObjectTable: fffff8a0025bd440  HandleCount: 1056.
    Image: explorer.exe
```

Now you can pass the process address for explorer.exe to the **!processirps** command. The following output shows that explorer.exe has IRPs queued to threads and IRPs queued to file objects.

```
2: kd> !processirps fffffa800688c940
**** PROCESS fffffa800688c940 (Image: explorer.exe) ****

Checking threads for IRPs.

  Thread fffffa800689f080:

    IRP fffffa80045ccc10 - Owned by \FileSystem\Ntfs for device fffffa8004f5c030
    IRP fffffa800454f650 - Owned by \FileSystem\Ntfs for device fffffa8004f5c030
    ...
    IRP fffffa80068e9c10 - Owned by \FileSystem\Ntfs for device fffffa8004f5c030

Checking file objects for IRPs.

  FileObject fffffa80068795e0 (handle 8bc):

    IRP fffffa8006590cf0 - Owned by \Driver\DeviceApi for device DeviceApi (fffffa800363ae40)

  ...

  FileObject fffffa8005bf59c0 (handle 900):

    IRP fffffa8006659010 - Owned by \Driver\DeviceApi for device DeviceApi (fffffa800363ae40)
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!processirps%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




