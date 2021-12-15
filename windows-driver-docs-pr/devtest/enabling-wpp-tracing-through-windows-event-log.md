---
title: How Do I Enable WPP Tracing Through the Windows Event Log Service
description: The Windows Event Log service supports WPP logging and decoding. This topic describes how to enable WPP tracing through the Windows Event Log service.
ms.date: 04/20/2017
---

# How to Enable WPP Tracing Through the Windows Event Log Service

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
