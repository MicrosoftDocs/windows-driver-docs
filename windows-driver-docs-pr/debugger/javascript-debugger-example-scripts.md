---
title: JavaScript Debugger Example Scripts
description: This topic provides the information on user and kernel mode JavaScript code samples, such as the Data Filtering Plug and Play Device Tree sample.
ms.assetid: F477430B-10C7-4039-9C5F-25556C306643
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JavaScript Debugger Example Scripts


This topic provides the following user and kernel mode JavaScript code samples.

-   [Data Filtering: Plug and Play Device Tree in KD (Kernel Mode)](#filter)
-   [Extend Devices Specific To Multimedia (Kernel Mode)](#multimedia)
-   [Adding Bus Information to \_DEVICE\_OBJECT (Kernel Mode)](#bus)
-   [Find an Application Title (User Mode)](#title)

## <span id="Working_with_Samples"></span><span id="working_with_samples"></span><span id="WORKING_WITH_SAMPLES"></span>Working with Samples


Use the general process to test any of the samples.

1. Determine if the sample JavaScript is intended for kernel or user mode debugging. Then either load an appropriate dump file or establish a live connection to a target system.

2. Use a text editor such as Notepad to create a text file named and save it with a .js file extension, such as *HelloWorld.js*

```javascript
// WinDbg JavaScript sample
// Says Hello World!

// Code at root will be run with .scriptrun and .scriptload
host.diagnostics.debugLog("***> Hello World! \n");

function sayHi()
{
   //Say Hi 
   host.diagnostics.debugLog("Hi from JavaScript! \n");
}
```

3. Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider.

```dbgcmd
0:000> .load jsprovider.dll
```

4. Use the [**.scriptrun (Run Script)**](-scriptrun--run-script-.md)command to load and execute the script. The .scriptrun command will run code at the root/top and the code under the function names *initializeScript* and *invokeScript*.

```dbgcmd
0:000> .scriptrun c:\WinDbg\Scripts\HelloWorld.js
JavaScript script successfully loaded from 'c:\WinDbg\Scripts\HelloWorld.js'
***> Hello World! 
```

5. If the script contains a uniquely named function, use the dx command to execute that function, that is located in Debugger.State.Scripts.*ScriptName*.Contents.*FunctionName*.

```dbgcmd
0:001> dx Debugger.State.Scripts.HelloWorld.Contents.sayHi()
Hi from JavaScript!
Debugger.State.Scripts.HelloWorld.Contents.sayHi()
```

Refer to [JavaScript Debugger Scripting](javascript-debugger-scripting.md) for additional information about working with JavaScript.

## <span id="Filter"></span><span id="filter"></span><span id="FILTER"></span>Data Filtering: Plug and Play Device Tree in KD (Kernel Mode)


This sample code filters the device node tree to display just devices that contain a path of PCI that are started.

This script is intended to support kernel mode debugging.

You can use the !devnode 0 1 command to display information about the device tree. For more information, see [**!devnode**](-devnode.md).

```javascript
// PlugAndPlayDeviceTree.js
// An ES6 generator function which recursively filters the device tree looking for PCI devices in the started state.
//
function *filterDevices(deviceNode)
{
    //
    // If the device instance path has "PCI" in it and is started (state == 776), yield it from the generator.
    //
    if (deviceNode.InstancePath.indexOf("PCI") != -1 && deviceNode.State == 776)
    {
        yield deviceNode;
    }
 
    //
    // Recursively invoke the generator for all children of the device node.
    //
    for (var childNode of deviceNode.Children)
    {
        yield* filterDevices(childNode);
    }
}
 
//
// A function which finds the device tree of the first session in the debugger and passes it to our filter function.
//
function filterAllDevices()
{
    return filterDevices(host.namespace.Debugger.Sessions.First().Devices.DeviceTree.First());
}
```

Either load a kernel dump file or establish a kernel mode connection to a target system.

```dbgcmd
0: kd> !load jsprovider.dll
```

```dbgcmd
0: kd> .scriptload c:\WinDbg\Scripts\deviceFilter.js
JavaScript script successfully loaded from 'c:\WinDbg\Scripts\deviceFilter.js'
```

Call the filterAllDevices() function.

```dbgcmd
0: kd> dx Debugger.State.Scripts.PlugAndPlayDeviceTree.Contents.filterAllDevices()
Debugger.State.Scripts.PlugAndPlayDeviceTree.Contents.filterAllDevices()                 : [object Generator]
    [0x0]            : PCI\VEN_8086&DEV_D131&SUBSYS_304A103C&REV_11\3&21436425&0&00
    [0x1]            : PCI\VEN_8086&DEV_D138&SUBSYS_304A103C&REV_11\3&21436425&0&18 (pci)
    [0x2]            : PCI\VEN_10DE&DEV_06FD&SUBSYS_062E10DE&REV_A1\4&324c21a&0&0018 (nvlddmkm)
    [0x3]            : PCI\VEN_8086&DEV_3B64&SUBSYS_304A103C&REV_06\3&21436425&0&B0 (HECIx64)
    [0x4]            : PCI\VEN_8086&DEV_3B3C&SUBSYS_304A103C&REV_05\3&21436425&0&D0 (usbehci)
    [0x5]            : PCI\VEN_8086&DEV_3B56&SUBSYS_304A103C&REV_05\3&21436425&0&D8 (HDAudBus)
...
```

Each of these objects presented above, automatically supports DML, and can be clicked through just as with any other dx query.

Alternatively to using this script, it is possible to use a LINQ query to accomplish a similar result.

```dbgcmd
0: kd> dx @$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.InstancePath.Contains("PCI") && n.State == 776)
@$cursession.Devices.DeviceTree.Flatten(n => n.Children).Where(n => n.InstancePath.Contains("PCI") && n.State == 776)  
    [0x0]            : PCI\VEN_8086&DEV_D131&SUBSYS_304A103C&REV_11\3&21436425&0&00
    [0x1]            : PCI\VEN_8086&DEV_D138&SUBSYS_304A103C&REV_11\3&21436425&0&18 (pci)
    [0x2]            : PCI\VEN_10DE&DEV_06FD&SUBSYS_062E10DE&REV_A1\4&324c21a&0&0018 (nvlddmkm)
    [0x3]            : PCI\VEN_8086&DEV_3B64&SUBSYS_304A103C&REV_06\3&21436425&0&B0 (HECIx64)
    [0x4]            : PCI\VEN_8086&DEV_3B3C&SUBSYS_304A103C&REV_05\3&21436425&0&D0 (usbehci)
    [0x5]            : PCI\VEN_8086&DEV_3B56&SUBSYS_304A103C&REV_05\3&21436425&0&D8 (HDAudBus)
...
```

## <span id="Multimedia"></span><span id="multimedia"></span><span id="MULTIMEDIA"></span>Extend Devices Specific To Multimedia (Kernel Mode)


This larger JavaScript example extends a kernel \_DEVICE\_OBJECT for information specific to multimedia and adds StreamingDevices to a debugger session.

This script is intended to support kernel mode debugging.

Note that the choice to extend Session with StreamingDevices is done for example purposes only. This should be either left to \_DEVICE\_OBJECT only or deeper inside a namespace under the existing .Devices.\* hierarchy.

```javascript
// StreamingFinder.js
// Extends a kernel _DEVICE_OBJECT for information specific to multimedia 
// and adds StreamingDevices to a debugger session.
//

"use strict";
 
function initializeScript()
{
    // isStreamingDeviceObject: 
    //
    // Returns whether devObj (as a _DEVICE_OBJECT -- not a pointer) looks like it is a device
    // object for a streaming device.
    //
    function isStreamingDeviceObject(devObj)
    {
        try
        {
            var devExt = devObj.DeviceExtension;
            var possibleStreamingExtPtrPtr = host.createPointerObject(devExt.address, "ks.sys", "_KSIDEVICE_HEADER **", devObj);
            var possibleStreamingExt = possibleStreamingExtPtrPtr.dereference().dereference();
            var baseDevice = possibleStreamingExt.BaseDevice;
 
            if (devObj.targetLocation == baseDevice.dereference().targetLocation)
            {
                return true;
            }
        }
        //
        // The above code expects to fail (walking into invalid or paged out memory) often.  A failure to read the memory
        // of the target process will result in an exception.  Catch such exception and indicate that the object does not
        // match the profile of a "streaming device object".
        //
        catch(exc)
        {   
        }
 
        return false;
    }
 
    // findStreamingFDO(pdo):
    //
    // From a physical device object, walks up the device stack and attempts to find a device which
    // looks like a streaming device (and is thus assumed to be the FDO).  pdo is a pointer to 
    // the _DEVICE_OBJECT for the pdo.
    //
    function findStreamingFDO(pdo)
    {
        for (var device of pdo.UpperDevices)
        {
            if (isStreamingDeviceObject(device.dereference()))
            {
                return device;
            }
        }
 
        return null;
    }
 
    // streamingDeviceList:
    //
    // A class which enumerates all streaming devices on the system.
    //
    class streamingDeviceList
    {
        constructor(session)
        {
            this.__session = session;
        }
 
        *[Symbol.iterator]()
        {
            //
            // Get the list of all PDOs from PNP using LINQ:
            //
            var allPDOs = this.__session.Devices.DeviceTree.Flatten(function(dev) { return dev.Children; })
                                                           .Select (function(dev) { return dev.PhysicalDeviceObject; });
 
            //
            // Walk the stack up each PDO to find the functional device which looks like a KS device.  This is
            // a very simple heuristic test: the back pointer to the device in the KS device extension is
            // accurate.  Make sure this is wrapped in a try/catch to avoid invalid memory reads causing
            // us to bail out.
            //
            // Don't even bother checking the PDO.
            //
            for (var pdo of allPDOs)
            {
                var fdo = findStreamingFDO(pdo);
                if (fdo != null)
                {
                    yield fdo;
                }
            }
        }
   }
 
    // streamingDeviceExtension:
    //
    // An object which will extend "session" and include the list of streaming devices.
    //
    class streamingDeviceExtension
    {
        get StreamingDevices()
        {
            return new streamingDeviceList(this);
        }
    };
 
    // createEntryList:
    //
    // An abstraction over the create entry list within a streaming device.
    //    
    class createEntryList
    {
        constructor(ksHeader)
        {
            this.__ksHeader = ksHeader;
        }
 
        *[Symbol.iterator]()
        {
            for (var entry of host.namespace.Debugger.Utility.Collections.FromListEntry(this.__ksHeader.ChildCreateHandlerList, "ks!KSICREATE_ENTRY", "ListEntry"))
            {
                                                            if (!entry.CreateItem.Create.isNull)
                {
                    yield entry;
                }
            }
        }
    }
 
    // streamingInformation:
    //
    // Represents the streaming state of a device.
    //    
    class streamingInformation
    {
        constructor(fdo)
        {
            this.__fdo = fdo;
 
            var devExt = fdo.DeviceExtension;
            var streamingExtPtrPtr = host.createPointerObject(devExt.address, "ks.sys", "_KSIDEVICE_HEADER **", fdo);
            this.__ksHeader = streamingExtPtrPtr.dereference().dereference();
        }
 
        get CreateEntries()
        {
            return new createEntryList(this.__ksHeader);
        }
    }
 
    // createEntryVisualizer:
    //
    // A visualizer for KSICREATE_ENTRY
    //
    class createEntryVisualizer
    {
        toString()
        {
            return this.CreateItem.ObjectClass.toString();
        }
 
        get CreateContext()
        {
            //
            // This is probably not entirely accurate.  The context is not *REQUIRED* to be an IUnknown.
            // More analysis should probably be performed.
            //
            return host.createTypedObject(this.CreateItem.Context.address, "ks.sys", "IUnknown", this);
        }
    }
 
    // deviceExtension:
    //
    // Extends our notion of a device in the device tree to place streaming information on
    // top of it.
    //
    class deviceExtension
    {
        get StreamingState()
        {
            if (isStreamingDeviceObject(this))
            {
                return new streamingInformation(this);
            }
 
            //
            // If we cannot find a streaming FDO, returning undefined will indicate that there is no value
            // to the property.
            //
            return undefined;
        }
    }
 
    return [new host.namedModelParent(streamingDeviceExtension, "Debugger.Models.Session"),
            new host.typeSignatureExtension(deviceExtension, "_DEVICE_OBJECT"),
            new host.typeSignatureRegistration(createEntryVisualizer, "KSICREATE_ENTRY")]
}
```

First load the script provider as described previously. Then load the script.

```dbgcmd
0: kd> .scriptload c:\WinDbg\Scripts\StreamingFinder.js
JavaScript script successfully loaded from 'c:\WinDbg\Scripts\StreamingFinder.js'
```

Then use the dx command to access the new StreamingDevices capabilities that the script provides.

```dbgcmd
0: kd> dx -r3 @$cursession.StreamingDevices.Select(d => d->StreamingState.CreateEntries)
@$cursession.StreamingDevices.Select(d => d->StreamingState.CreateEntries)                
    [0x0]            : [object Object]
        [0x0]            : "e0HDMIOutTopo" [Type: KSICREATE_ENTRY]
            [<Raw View>]     [Type: KSICREATE_ENTRY]
            CreateContext    [Type: CPortTopology]
    [0x1]            : [object Object]
        [0x0]            : "AnalogDigitalCaptureTopo" [Type: KSICREATE_ENTRY]
            [<Raw View>]     [Type: KSICREATE_ENTRY]
            CreateContext    [Type: CPortTopology]
        [0x1]            : "AnalogDigitalCapture1Topo" [Type: KSICREATE_ENTRY]
            [<Raw View>]     [Type: KSICREATE_ENTRY]
            CreateContext    [Type: CPortTopology]
        [0x2]            : "AnalogDigitalCapture2Topo" [Type: KSICREATE_ENTRY]
            [<Raw View>]     [Type: KSICREATE_ENTRY]
            CreateContext    [Type: CPortTopology]
        [0x3]            : "AnalogDigitalCapture2Wave" [Type: KSICREATE_ENTRY]
            [<Raw View>]     [Type: KSICREATE_ENTRY]
            CreateContext    [Type: CPortWaveRT]
        [0x4]            : "HeadphoneTopo" [Type: KSICREATE_ENTRY]
            [<Raw View>]     [Type: KSICREATE_ENTRY]
            CreateContext    [Type: CPortTopology]
        [0x5]            : "RearLineOutTopo" [Type: KSICREATE_ENTRY]
            [<Raw View>]     [Type: KSICREATE_ENTRY]
            CreateContext    [Type: CPortTopology]
        [0x6]            : "RearLineOutWave" [Type: KSICREATE_ENTRY]
            [<Raw View>]     [Type: KSICREATE_ENTRY]
            CreateContext    [Type: CPortWaveRT]
    [0x2]            : [object Object]
        [0x0]            : "GLOBAL" [Type: KSICREATE_ENTRY]
            [<Raw View>]     [Type: KSICREATE_ENTRY]
            CreateContext    [Type: IUnknown]
```

## <span id="Bus"></span><span id="bus"></span><span id="BUS"></span>Adding Bus Information to \_DEVICE\_OBJECT (Kernel Mode)


This script extends the visualization of \_DEVICE\_OBJECT to add a BusInformation field which has PCI specific information underneath it. The manner and namespacing of this sample are still being discussed. It should be considered a sample of the capabilities of the JavaScript provider.

This script is intended to support kernel mode debugging.

```javascript
"use strict";

/*************************************************
DeviceExtensionInformation.js:

An example which extends _DEVICE_OBJECT to add bus specific information
to each device object.

NOTE: The means of conditionally adding and the style of namespacing this
are still being discussed.  This currently serves as an example of the capability
of JavaScript extensions.

*************************************************/

function initializeScript()
{
    // __getStackPDO():
    //
    // Returns the physical device object of the device stack whose device object
    // is passed in as 'devObj'.
    //
    function __getStackPDO(devObj)
    {
        var curDevice = devObj;
        var nextDevice = curDevice.DeviceObjectExtension.AttachedTo;
        while (!nextDevice.isNull)
        {
            curDevice = nextDevice;
            nextDevice = curDevice.DeviceObjectExtension.AttachedTo;
        }
        return curDevice;
    }
    
    // pciInformation:
    //
    // Class which abstracts our particular representation of PCI information for a PCI device or bus
    // based on a _PCI_DEVICE structure or a _PCI_BUS structure.
    //
    class pciInformation
    {
        constructor(pciDev)
        {
            this.__pciDev = pciDev;
            this.__pciPDO = __getStackPDO(this.__pciDev);
            this.__isBridge = (this.__pciDev.address != this.__pciPDO.address);
            
            if (this.__isBridge)
            {
                this.__deviceExtension = host.createTypedObject(this.__pciPDO.DeviceExtension.address, "pci.sys", "_PCI_DEVICE", this.__pciPDO);
                this.__busExtension = host.createTypedObject(this.__pciDev.DeviceExtension.address, "pci.sys", "_PCI_BUS", this.__pciPDO);
                
                this.__hasDevice = (this.__deviceExtension.Signature == 0x44696350); /* 'PciD' */
                this.__hasBus = (this.__busExtension.Signature == 0x42696350); /* 'PciB' */
                
                if (!this.__hasDevice && !this.__hasBus)
                {
                    throw new Error("Unrecognized PCI device extension");
                }
            }
            else
            {
                this.__deviceExtension = host.createTypedObject(this.__pciPDO.DeviceExtension.address, "pci.sys", "_PCI_DEVICE", this.__pciPDO);
                
                this.__hasDevice = (this.__deviceExtension.Signature == 0x44696350); /* 'PciD' */
                this.__hasBus = false;
                
                if (!this.__hasDevice)
                {
                    throw new Error("Unrecognized PCI device extension");
                }
            }
        }
        
        toString()
        {
            
            if (this.__hasBus && this.__hasDevice)
            {
                return "Bus: " + this.__busExtension.toString() + " Device: " + this.__deviceExtension.toString();
            }
            else if (this.__hasBus)
            {
                return this.__busExtension.toString();
            }
            else
            {
                return this.__deviceExtension.toString();
            }
        }
        
        get Device()
        {
            if (this.__hasDevice)
            {
                // NatVis supplies the visualization for _PCI_DEVICE
                return this.__deviceExtension;
            }
            
            return undefined;
        }
        
        get Bus()
        {
            if (this.__hasBus)
            {
                // NatVis supplies the visualization for _PCI_BUS
                return this.__busExtension;
            }
            
            return undefined;
        }
    }
    
    // busInformation:
    //
    // Our class which does analysis of what bus a particular device is on and places information about
    // about that bus within the _DEVICE_OBJECT visualization.
    //
    class busInformation
    {
        constructor(devObj)
        {
            this.__devObj = devObj;
        }
        
        get PCI()
        {
            //
            // Check the current device object.  This may be a PCI bridge
            // in which both the FDO and PDO are relevant (one for the bus information
            // and one for the bridge device information).
            //
            var curName = this.__devObj.DriverObject.DriverName.toString();
            if (curName.includes("\\Driver\\pci"))
            {
                return new pciInformation(this.__devObj);
            }
            
            var stackPDO = __getStackPDO(this.__devObj);
            var pdoName = stackPDO.DriverObject.DriverName.toString();
            if (pdoName.includes("\\Driver\\pci"))
            {
                return new pciInformation(stackPDO);
            }
            
            return undefined;
        }
    }
    
    // busInformationExtension:
    //
    // An extension placed on top of _DEVICE_OBJECT in order to provide bus analysis and bus specific
    // information to the device.
    //
    class busInformationExtension
    {
        get BusInformation()
        {
            return new busInformation(this);
        }
    }
    
    return [new host.typeSignatureExtension(busInformationExtension, "_DEVICE_OBJECT")];
}
```

First load the script provider as described previously. Then load the script.

```dbgcmd
0: kd> .scriptload c:\WinDbg\Scripts\DeviceExtensionInformation.js
JavaScript script successfully loaded from 'c:\WinDbg\Scripts\DeviceExtensionInformation.js'
```

We need to locate the address of the device object we are interested in. In this example, we will examine the audio HDAudBus driver.

```dbgcmd
0: kd>  !drvobj HDAudBus
Driver object (ffffb60757a4ae60) is for:
 \Driver\HDAudBus
Driver Extension List: (id , addr)
(fffff8050a9eb290 ffffb60758413180)  
Device Object list:
ffffb60758e21810  ffffb60757a67c60
```

After the script is loaded use the dx command to display bus information for device objects.

```dbgcmd
0: kd> dx -r1 (*((ntkrnlmp!_DEVICE_OBJECT *)0xffffe00001b567c0))
(*((ntkrnlmp!_DEVICE_OBJECT *)0xffffe00001b567c0))                 : Device for "\Driver\HDAudBus" [Type: _DEVICE_OBJECT]
    [<Raw View>]     [Type: _DEVICE_OBJECT]
    Flags            : 0x2004
    UpperDevices     : None
    LowerDevices     : Immediately below is Device for "\Driver\ACPI" [at 0xffffe000003d9820]
    Driver           : 0xffffe00001ccd060 : Driver "\Driver\HDAudBus" [Type: _DRIVER_OBJECT *]
    BusInformation   : [object Object]

0: kd> dx -r1 (*((ntkrnlmp!_DEVICE_OBJECT *)0xffffe00001b567c0)).@"BusInformation"
(*((ntkrnlmp!_DEVICE_OBJECT *)0xffffe00001b567c0)).@"BusInformation"                 : [object Object]
    PCI              :  (d=0x14 f=0x2) Vendor=0x1022 Device=0x780d Multimedia Device / Unknown Sub Class

0: kd> dx -r1 (*((ntkrnlmp!_DEVICE_OBJECT *)0xffffe00001b567c0)).@"BusInformation".@"PCI"
(*((ntkrnlmp!_DEVICE_OBJECT *)0xffffe00001b567c0)).@"BusInformation".@"PCI"                 :  (d=0x14 f=0x2) Vendor=0x1022 Device=0x780d Multimedia Device / Unknown Sub Class
    Device           :  (d=0x14 f=0x2) Vendor=0x1022 Device=0x780d Multimedia Device / Unknown Sub Class [Type: _PCI_DEVICE]

0: kd> dx -r1 (*((pci!_PCI_DEVICE *)0xffffe000003fe1b0))
(*((pci!_PCI_DEVICE *)0xffffe000003fe1b0))                 :  (d=0x14 f=0x2) Vendor=0x1022 Device=0x780d Multimedia Device / Unknown Sub Class [Type: _PCI_DEVICE]
    [<Raw View>]     [Type: _PCI_DEVICE]
    Device           : 0xffffe000003fe060 : Device for "\Driver\pci" [Type: _DEVICE_OBJECT *]
    Requirements    
    Resources       

0: kd> dx -r1 (*((pci!_PCI_DEVICE *)0xffffe000003fe1b0)).@"Resources"
(*((pci!_PCI_DEVICE *)0xffffe000003fe1b0)).@"Resources"                
    BaseAddressRegisters
    Interrupt        : Line Based -- Interrupt Line = 0x10 [Type: _PCI_DEVICE_INTERRUPT_RESOURCE]

0: kd> dx -r1 (*((pci!_PCI_DEVICE *)0xffffe000003fe1b0)).@"Resources".@"BaseAddressRegisters"
(*((pci!_PCI_DEVICE *)0xffffe000003fe1b0)).@"Resources".@"BaseAddressRegisters"                
    [0x0]            : Memory Resource: 0xf0340000 of length 0x4000 [Type: _CM_PARTIAL_RESOURCE_DESCRIPTOR]
```

## <span id="Title"></span><span id="title"></span><span id="TITLE"></span>Find an Application Title (User Mode)


This example iterates through all the threads in the debugger's current process, finds a frame which includes *\_\_mainCRTStartup* and then returns the string from the StartupInfo.lpTitle within the CRT's startup. This script shows examples of iteration, string manipulation, and LINQ queries within JavaScript.

This script is intended to support user mode debugging.

```javascript
// TitleFinder.js
// A function which uses just JavaScript concepts to find the title of an application
//
function findTitle()
{
    var curProcess = host.currentProcess;
    for (var thread of curProcess.Threads)
    {
        for (var frame of thread.Stack.Frames)
        {
            if (frame.toString().includes("__mainCRTStartup"))
            {
                var locals = frame.LocalVariables;
 
                //
                // locals.StartupInfo.lpTitle is just an unsigned short *.  We need to actually call an API to
                // read the UTF-16 string in the target address space.  This would be true even if this were
                // a char* or wchar_t*.
                //
                return host.memory.readWideString(locals.StartupInfo.lpTitle);
            }
        }
    }
}
 
//
// A function which uses both JavaScript and integrated LINQ concepts to do the same.
//
function findTitleWithLINQ()
{
    var isMainFrame = function(frame) { return frame.toString().includes("__mainCRTStartup"); };
    var isMainThread = function(thread) { return thread.Stack.Frames.Any(isMainFrame); };
 
    var curProcess = host.currentProcess;
    var mainThread = curProcess.Threads.Where(isMainThread).First();
    var mainFrame = mainThread.Stack.Frames.Where(isMainFrame).First();
 
    var locals = mainFrame.LocalVariables;
 
    //
    // locals.StartupInfo.lpTitle is just an unsigned short *.  We need to actually call an API to
    // read the UTF-16 string in the target address space.  This would be true even if this were
    // a char* or wchar_t*.
    //
    return host.memory.readWideString(locals.StartupInfo.lpTitle);
}
```

```dbgcmd
0: kd> .scriptload c:\WinDbg\Scripts\TitleFinder.js
JavaScript script successfully loaded from 'c:\WinDbg\Scripts\TitleFinder.js'
```

Calling the findTitle() function returns notepad.exe

```dbgcmd
0:000> dx Debugger.State.Scripts.TitleFinder.Contents.findTitle()
Debugger.State.Scripts.TitleFinder.Contents.findTitle() : C:\Windows\System32\notepad.exe
```

Calling the LINQ version, findTitleWithLINQ() also returns notepad.exe

```dbgcmd
0:000> dx Debugger.State.Scripts.TitleFinder.Contents.findTitleWithLINQ()
Debugger.State.Scripts.titleFinder.Contents.findTitleWithLINQ() : C:\Windows\System32\notepad.exe
```

## <span id="related_topics"></span>Related topics


[JavaScript Debugger Scripting](javascript-debugger-scripting.md)

 

 






