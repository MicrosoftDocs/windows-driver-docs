---
title: How Do I Enable WPP Tracing Through the Windows Event Log Service
description: .
ms.assetid: cd5dad3e-fa25-4ec2-bc17-9332b4c00d17
---

# How Do I Enable WPP Tracing Through the Windows Event Log Service?


The Windows Event Log service supports WPP logging and decoding. This topic describes how to enable WPP tracing through the Windows Event Log service.

Enabling WPP tracing in this scenario requires no extra work to the WPP provider. However, to use the Windows Event Log service, you must supply a manifest and an Event Log provider. To enable WPP tracing, declare a debug channel and specify the associated control GUID as declared for your WPP provider.

For example:

```xsd
<instrumentationManifest
    xmlns="http://schemas.microsoft.com/win/2004/08/events" 
    xmlns:win="http://manifests.microsoft.com/win/2004/08/windows/events"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema"  xsi:schemaLocation="http://schemas.microsoft.com/win/2004/08/events eventman.xsd"  
    >
   <instrumentation>
        <events>
            <provider name="Microsoft-Windows-mySampleProvider" 
                guid="{61CE3EC9-E5E8-4b96-A451-74631A6E0D5C}" 
                >
          <channel
        chid="MS_WINDOWS_GE_DEBUG"
        enabled="false"
        isolation="System"
        message="$(string.Microsoft-Windows-GenerateEvent.channel.CHANNEL_DEBUG.message)"
        name="Microsoft-Windows-GenerateEvent/Debug"
        symbol="CHANNEL_DEBUG"
        type="Debug"
        >
        <publishing>
          <level>2</level>
          <keywords>0xFFFFFFFF</keywords>
          <controlGuid>{d58c126f-b309-11d1-969e-0000f875a5bc}</controlGuid>
        </publishing>
        </channel>
       </provider>
    </events>
   </instrumentation>
</instrumentationManifest>
```

WPP tracing is not meant to be enabled all the time, so by default the **enable** attribute in the manifest should be set to false. When WPP tracing is needed, change the attribute in the manifest, so that **enabled="true"**.

You cannot specify or individually select control bits. To enable all WPP events to this channel, specify a keyword value of 0XFFFFFFFF. Internally, control bits map to keywords; if you know which bit maps to a specific keyword, you can select that keyword to get a specific set of events. In the example manifest, the keyword value is 0xFFFF because less than 16 WPP control bits are needed. To get a specific set of events after installation, you may change the keywords using the wevtutil.exe command-line utility. The command is:

**wevtutil** **sl** *&lt;channel name&gt;***/k:***&lt;keyword value corresponding to control bit&gt;*

Note that the channel must first be disabled to change the keyword value.

Declaring a channel in this manner enables both the WPP provider (whose control GUID is specified) and the Event Log provider (under which this channel is declared) to access the debug channel, so either provider can write to this channel. WPP events or normal ETW events can now be seen under this channel through the event viewer.

WPP events are not decoded. To get message strings associated with these events, place the TMF files in the %windir%\\System32\\winevt\\TraceFormat directory. You can get the TMF files by using a utility such as Tracepdb.exe, which takes the PDB file for input and returns TMF files.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20Do%20I%20Enable%20WPP%20Tracing%20Through%20the%20Windows%20Event%20Log%20Service?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




