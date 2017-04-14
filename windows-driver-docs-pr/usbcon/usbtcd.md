---
Description: USBTCD is the combination of a user-mode application and kernel-mode driver.
title: USBTCD
author: windows-driver-content
---

# USBTCD


USBTCD is the combination of a user-mode application and kernel-mode driver. The tool performs read and write operations. It initiates control, bulk, isochronous, data transfers of various transfer lengths to and from the test device. For a SuperMUTT device, USBTCD transfers data to streams supported by a bulk endpoint. It can also send the transfer buffer as chained MDLs. In that case, you can specify the number of segments in the transfer buffer.

The USBTCD files are included in the [MUTT Software Package](http://msdn.microsoft.com/windows/hardware/jj590752).

## USBTCD


To use these commands, the USBTCD driver (USBTCD.sys) must be loaded as the function driver for the device. To load the driver for the device, run MUTTUtil and specify **USBTCD.inf**. This tool loads **USBTCD.sys** for all attached USB devices.

``` syntax
c:\Program Files (x86)\USBTest\x64>MuttUtil.exe -UpdateDriver usbtcd.inf
Return value: 0


c:\Program Files (x86)\USBTest\x64>MuttUtil.exe -list
       :    : HARDWARE ID                    :  PROBLEM CODE  : DRIVER
DEVICE :  0 : USB\VID_045E&PID_078E&REV_8011 :             0  : USBTCD
Return value: 1
```

You can use the following commands to measure performance for transfers to and from the bulk endpoints of a SuperMUTT device.

**Usbtcd –perf –read 1 100 2 10240000 0**

**Usbtcd –perf –write 1 100 0 10240000 0**

In the preceding command, USBTCD reads 10240000 bytes from pipe 2. In the second command, USBTCD starts a write operation where 10240000 bytes are sent to the pipe 0. For both commands, the tool performs the operation 100 times and does not specify a timeout value.

These commands are used to measure performance of bulk endpoints of the MUTT device. Notice that the transfer sizes are reduced in this case.

**Usbtcd –perf –read 1 100 2 512000 0**

**Usbtcd –perf –write 1 100 0 512000 0**

These commands measure the performance of data transfers to streams of bulk endpoints of the SuperMUTT device. Currently, the device firmware tries to switch streams every millisecond be sending an ERDY together with the new stream number to the host. That is implemented with a timer inside the device.

**Usbtcd –sread 1 100 7 1 1024 0**

**Usbtcd –swrite 1 100 6 1 1024 0**

In the preceding command, USBTCD reads and writes to a particular stream in the bulk endpoint of a SuperMUTT device. In the first command, the tool starts a worker thread that reads 1024 bytes from stream 1 associated with pipe 7. Similarly, the second command writes 1024 bytes to stream 1 associated with pipe 6. For both commands, the tool performs the operation 100 times and does not specify a timeout value.

To view help on USBTCD, run the following command:

**usbtcd -?**

The command shows information on the command-line options. Transfer sizes, verbosity, transfer timeouts, and more can be specified on the command line.

## Related topics
[USB test tools](usb-test-tools.md)  
[Tools in the MUTT software package](mutt-software-package.md)  
[Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USBTCD%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


