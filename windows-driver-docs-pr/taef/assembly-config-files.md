---
title: Assembly Config Files
description: Assembly Config Files
ms.assetid: 53BAC457-BB6A-44a8-AD8D-3B621F41A245
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Assembly Config Files


TAEF supports test assembly configuration files. A configuration file should have the same name as your test assembly + ".config". If you have a test assembly that is named **MyUnitTests.dll**, your configuration file should be named **MyUnitTests.dll.config**.

The configuration file should be placed in the same directory as your test assembly file.

## <span id="dotnet_cf"></span><span id="DOTNET_CF"></span>.NET Configuration Files


The .NET Configuration files are XML files in the following form:

```
<configuration>
    <appSettings>
        <add key="AssemblySetup" value="Assembly setup configuration information"/>
        <add key="ClassSetup" value="Class setup configuration information"/>
        <add key="TestSetup" value="Test setup configuration information"/>
        <add key="Test" value="Test configuration information"/>
    </appSettings>
</configuration>
```

Note, the configuration file is a collection of name / value pairs. See MSDN for more info.

## <span id="reading_cf"></span><span id="READING_CF"></span>Reading the Configuration File from Your Tests


You can use the **System.Configuration.ConfigurationManager** class to read data from your configuration files. For example,

```
NameValueCollection appStgs = ConfigurationManager.AppSettings;
Log.Comment(appStgs["AssemblySetup"]);
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Assembly%20Config%20Files%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




