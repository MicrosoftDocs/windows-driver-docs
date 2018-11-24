---
title: Assembly Config Files
description: Assembly Config Files
ms.assetid: 53BAC457-BB6A-44a8-AD8D-3B621F41A245
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Assembly Config Files


TAEF supports test assembly configuration files. A configuration file should have the same name as your test assembly + ".config". If you have a test assembly that is named **MyUnitTests.dll**, your configuration file should be named **MyUnitTests.dll.config**.

The configuration file should be placed in the same directory as your test assembly file.

## <span id="dotnet_cf"></span><span id="DOTNET_CF"></span>.NET Configuration Files


The .NET Configuration files are XML files in the following form:

```cpp
<configuration>
    <appSettings>
        <add key="AssemblySetup" value="Assembly setup configuration information"/>
        <add key="ClassSetup" value="Class setup configuration information"/>
        <add key="TestSetup" value="Test setup configuration information"/>
        <add key="Test" value="Test configuration information"/>
    </appSettings>
</configuration>
```

Note, the configuration file is a collection of name / value pairs.

## <span id="reading_cf"></span><span id="READING_CF"></span>Reading the Configuration File from Your Tests


You can use the **System.Configuration.ConfigurationManager** class to read data from your configuration files. For example,

```cpp
NameValueCollection appStgs = ConfigurationManager.AppSettings;
Log.Comment(appStgs["AssemblySetup"]);
```

 

 





