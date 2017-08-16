---
title: Building a Basic v4 Printer Driver
author: windows-driver-content
description: Build a basic v4 printer driver by using the driver development Wizard in Microsoft Visual Studio 2013 to select the minimum set of features to create a functional printer driver.
ms.assetid: 6E50CD69-D385-4724-B6B1-85D42EFFC6F0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Building a Basic v4 Printer Driver


Build a basic v4 printer driver by using the driver development Wizard in Microsoft Visual Studio 2013 to select the minimum set of features to create a functional printer driver.

The instructions in this topic will focus on the steps required for building a driver, and will not explain the many printer driver options available in the Wizard. The intent of this topic is to provide an introduction to the process involved when developing a printer driver in Visual Studio 2013. A more detailed look at the printer driver options is provided in [Exploring the Driver Options in the Wizard](exploring-the-driver-options-in-the-wizard.md).

**Instructions**

## Select features for the basic driver


1. In Visual Studio, in the main menu, click **File** &gt; **New** &gt; **Project**.

2. In the **New Project** window, in the top-right search box, type *printer driver v4* and press enter. This will retrieve all driver templates whose names contain the search text.

3. In the middle pane, select **Printer Driver V4**.

4. Type a name for your driver in the **Name** field, and then click **OK**. For example, you could type *MyV4PrintDriver*.

5. In the **Create a v4 Print Driver Wizard**, under **Choose the driver rendering type:**, click **V4 print driver with custom rendering filters (accepts XPS only)**.

6. Leave all other options at their default settings and click **Next**.

7. In the **Setup information** section of the Wizard, leave all options at their default settings, then click **Next**.

8. In the **Setup information (page 2)** section of the Wizard, leave all options at their default settings, then click **Next**.

Microsoft Visual Studio uses the preceding selections to generate the project files for *MyV4PrintDriver*.

## Verify the generated driver files


1. Navigate to the folder for the generated driver files. For example, if you named your project *MyV4PrintDriver*, then by default, the files would be saved to the following location: *My Documents &gt; Visual Studio 2013 &gt; Projects &gt; MyV4PrintDriver &gt; MyV4PrintDriver*.

2. Verify that the folder contains the following files:

| File name                                              | File type                                                  |
|--------------------------------------------------------|------------------------------------------------------------|
| MyV4PrintDriver-manifest.ini                           | Configuration settings file (a.k.a. print driver manifest) |
| MyV4PrintDriver.gpd                                    | Printer description file                                   |
| MyV4PrintDriverPackage-Intellisense.js                 | JavaScript file for Intellisense                           |
| MyV4PrintDriverRenderFilter-Intellisense-Windows8.1.js | JavaScript file for Intellisense                           |
| MyV4PrintDriverRenderFilter.ini                        | Setup information file                                     |
| MyV4PrintDriverRenderFilter.vcxproj.filters            | C++ Project filters file                                   |
| MyV4PrintDriverRenderFilter.vcxproj                    | Project file                                               |

 

Notice from the preceding table that one of the files that is created is an INF file. Note that Visual Studio created a skeletal INF file that has to be completed so that it can be used to install the driver.

## Complete the INF file


### Configure the \[Version\] section


1. Check and make sure that you see this line:

**ClassVer**=4.0

2. Check and make sure that you see this line:

**Signature**=”$WINDOWS NT$”

### Configure the \[SourceDiskFiles\] section


Type the following lines:

```Text
MyV4PrinterDriver.gpd=1
MyV4PrinterDriver-manifest.ini=1
MyV4PrinterDriverRenderFilter-PipelineConfig.xml=1
MyV4PrintDriverRenderFilter.dll=1
```

### Create a section called \[DriverInstall\] at the bottom of the INF file, and configure it


Type the following line in the newly created \[DriverInstall\] section:

**CopyFiles**=DriverFiles

### Create a section called \[DriverFiles\] at the bottom of the INF file, and configure it


Type the following lines in the newly created \[DriverFiles\] section:

```Text
MyV4PrinterDriver.gpd
MyV4PrinterDriver-manifest.ini
MyV4PrinterDriverRenderFilter-PipelineConfig.xml
MyV4PrintDriverRenderFilter.dll
```

### Configure the \[Standard.NT$ARCH$\] section


Type the following lines to target a particular printer model. For example, if the model of your printer is Fabrikam1234, then you would type the following:

```Text
“Model name”=DriverInstall, USBPRINT\\Fabrikam1234
“Model name”=DriverInstall, WSDPRINT\\Fabrikam1234
```

### Add **PrinterDriverID** to the INF file


1. In Visual Studio, in the Solution Explorer, expand the *MyV4PrinterDriver Package* node.

2. Click Driver Files, then in the **Properties** window look at the value for the Unique Identifier field. This is the driver ID (the GUID). Highlight it and copy it

3. In the INF file, in the \[Standard.NT$ARCH$\] section, type the following line:

“Model name”=DriverInstall,

And then after the comma, paste the GUID that you copied in the preceding step. The completed \[Standard.NT$ARCH$\] section should like the following:

```Text
“Model name”=DriverInstall, USBPRINT\\Fabrikam1234
“Model name”=DriverInstall, WSDPRINT\\Fabrikam1234
“Model name”=DriverInstall, {GUID}
```

### Configure the \[String\] section

1. Type the following, to provide a manufacturer’s name for the target printer. For example, if your company’s name is My Company, you would type the following:

**ManufacturerName** = “My Company”

2. Save the INF file.

When you complete the INF file, it should look like the following. Note that in place of the *{GUID}* entry that is shown in this sample INF file, your INF file should contain the GUID that you retrieved using the steps in the preceding *Add PrinterDriverID to the INF file* section.

```Text
[Version]
Signature="$Windows NT$"
Class=Printer
ClassGuid={4D36E979-E325-11CE-BFC1-08002BE10318}
Provider=%ManufacturerName%
CatalogFile=MyV4PrinterDriver.cat
ClassVer=4.0
DriverVer=03/17/2014,1.0.0.0

[DestinationDirs]
DefaultDestDir = 66000

[SourceDisksNames]
1 = %DiskName%,,,""

[SourceDisksFiles]
MyV4PrinterDriver.gpd=1
MyV4PrinterDriver-manifest.ini=1
MyV4PrinterDriverRenderFilter-PipelineConfig.xml=1
MyV4PrintDriverRenderFilter.dll=1

[Manufacturer]
%ManufacturerName%=Standard,NT$ARCH$

[Standard.NT$ARCH$]
“Model name”=DriverInstall, USBPRINT\Fabrikam1234
“Model name”=DriverInstall, WSDPRINT\Fabrikam1234
“Model name”=DriverInstall, {GUID}

[DriverInstall]
CopyFiles=DriverFiles

[DriverFiles]
MyV4PrinterDriver.gpd
MyV4PrinterDriver-manifest.ini
MyV4PrinterDriverRenderFilter-PipelineConfig.xml
MyV4PrintDriverRenderFilter.dll

[Strings]
ManufacturerName="My Company"
DiskName="MyV4PrinterDriver Installation Disk"
```

## Configure driver solution for debugging and deployment


1. In the Solution Explorer, right-click *MyV4PrinterDriver Package*, then click **Properties**.

2. In the **MyV4PrinterDriver Package Property Pages** window, expand **Configuration Properties** in the left pane.

3. Expand **Driver Install**, then click **Deployment** do the following in the right pane:

-   Click **Enable deployment**
-   Check **Remove previous driver versions before deployment**
-   Ensure that the **Target Computer Name** is configured. If it isn’t, click “…” and follow the prompts in the **Computer Configuration** wizard to set up a remote target computer
-   Select **Install and Verify**, then select **Default Printer Driver Package Installation Task** from the drop-down box
-   Type the name of the driver in the **Optional Arguments** field (without any quotes around the name)
-   Click **OK**

## Configure Driver Signing


1. In the Solution Explorer, right-click *MyV4PrinterDriver Package*, then click **Properties**.

2. In the **MyV4PrinterDriver Package Property Pages** window, expand **Configuration Properties** in the left pane.

3. Expand **Driver Signing**, then click **General.**

4. In the right pane, confirm that **Sign Mode** is set to Test Sign.

5. Click **Test Certificate**, then select &lt;Create Test Certificate…&gt; from the drop-down box.

6. Click **TimeStampServer**, then select Verisign from the drop-down box.

7. Click **OK.**

## Build and deploy the driver


1. In Solution Explorer, right-click **Solution MyV4PrinterDriver (3 projects)**, and click **Build Solution**.

2. When the Build process is complete the driver will automatically be installed. Make sure that there are no errors in the Output window.

## Test the driver


Create a print queue using either plug-and-play or the Add Printer Wizard.

For more information about INF files for the v4 printer driver, see [V4 Driver INF](v4-driver-inf.md).

**Note**  
In addition to the files in the preceding table, notice that a *MyV4PrintDriver Render Filter* folder was created. This is the render filter project template and it provides a good foundation for building an XPS rendering filter and an XPS filter pipeline configuration file. For more information about XPS rendering filters, see [XPSDrv Render Module](xpsdrv-render-module.md), and to see an example of an XPS rendering filter, see the [XPS Rasterization Filter Service](http://go.microsoft.com/fwlink/p/?LinkId=617951) sample.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Building%20a%20Basic%20v4%20Printer%20Driver%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


