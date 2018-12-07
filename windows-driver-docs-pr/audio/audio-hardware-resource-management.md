---
title: Audio Hardware Resource Management
description: Windows 10 includes the ability to express concurrency constraints using and XML file.
ms.assetid: 6E94529E-F3F0-4DC5-AF8B-F896A4F991E3
ms.date: 10/29/2017
ms.localizationpriority: medium
---

# Audio Hardware Resource Management

Windows 10 includes the ability to express concurrency constraints using and XML file. On resource constrained mobile devices the ability to specify priority for specific audio streams can enhance the customer experience.

**Note**   This mechanism is only available in phones and tablets.
 
One challenge with creating a good audio experience on a low cost mobile device, is that some devices have various concurrency constraints. For example, it is possible that the device can only play up to 6 audio streams concurrently and supports only 2 offload streams. When there is an active phone call on a mobile device, it is possible that the device supports only 2 audio streams. When the device is capturing audio, the device can only play up to 4 audio streams.

Windows 10 includes a mechanism to express concurrency constraints to insure that high-priority audio streams and cellular phone calls will be able to play. If the system does not have enough resources, then low priority streams are terminated. This mechanism is only available in phones and tablets not on desktops or laptops.

To specify constraints complete these two steps.

- Create a concurrency constraints XML file as described in [Specify Concurrency Constraints](#specify_concurrency_constraints).
- Configure a registry entry to use the custom concurrency constraints XML file as described in [Registry\_Key\_Configuration](#registry_key_configuration).

## <span id="Specify_Concurrency_Constraints"></span><span id="specify_concurrency_constraints"></span><span id="SPECIFY_CONCURRENCY_CONSTRAINTS"></span>Specify Concurrency Resource Constraints


The XML constraints file is made up of three sections. The first required section is defined by &lt;Limits&gt; &lt;/Limits&gt;. This section can be used to define up to fifteen resource restraints. For example you could define constraints for the maximum number of rendering stream and the maximum number of streams that can be off loaded.

```xml
<?xml version="1.0" encoding="utf-8"?>
<ConstraintModel>
  
  <Limits> 
    <Resource>
      <ID>MaxRender</ID>
      <Consumption>6</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOffLoad</ID>
      <Consumption>2</Consumption>
    </Resource>
    ...

  </Limits>
```

The next section of the XML file defines one or more lists of exclusive endpoints, with each list containing two or more endpoints. These are endpoints that, that cannot be active at the same time. This section is optional.

For example, if the audio hardware has both HandsetSpeaker and WiredHeadsetSpeaker wired to the same DAC, that cannot be active at the same time, these should be in the same ExclusiveEndpoints list.

This section can have multiple &lt;ExclusiveEndpoints&gt; nodes. Each ExclusiveEndpoints node contains two or more Endpoint nodes. Each Endpoint node contains HWID, TopologyName, and PinId.

```xml
  <ExclusiveEndpoints>
    <Endpoint>
      <HWID>Root\sysvad_PhoneAudioSample</HWID>
      <!-- Example of h/w id specified in phoneaudiosample.inf -->
      <TopologyName>TopologySpeaker</TopologyName>
      <!-- Topology filter reference string-->
      <PinId>1</PinId>
      <!-- KSPIN_TOPO_LINEOUT_DEST -->
    </Endpoint>
    <Endpoint>
      <!-- Example of h/w id specified in phoneaudiosample.inf -->
      <HWID>Root\sysvad_PhoneAudioSample</HWID>
      <!-- Topology filter reference string-->
      <TopologyName>TopologyHandsetSpeaker</TopologyName>
      <!-- KSPIN_TOPO_LINEOUT_DEST -->
      <PinId>1</PinId>
    </Endpoint>
  </ExclusiveEndpoints>
```

The last required section of the XML file defines various resource consumers. This section of the file contains multiple &lt;ResourceConsumer&gt; entries. Each entry identifies information about a resource consumer and their associated resources use. Each resource that is used, must be previously defined in the &lt;Limits&gt; section.

```xml
  <ResourceConsumer>
    <!-- Active Phone call -->
    <ConsumerInfo>
      <PhoneCall>
        <CallState>Active</CallState>
      </PhoneCall>
    </ConsumerInfo>
    <Resource>
      <ID>MaxRender</ID>
      <Consumption>2</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOffLoad</ID>
      <Consumption>2</Consumption>
    </Resource>
    ...
  </ResourceConsumer>
```

As audio resources are used, the audio service tracks the resources. When insufficient resources are available, either lower priority streams are terminated or the current resource request fails if existing resource consumers are higher priority.

These are the valid &lt;ConsumerInfo&gt; entries.

-   &lt;PhoneCall&gt; - The &lt;Phonecall&gt; node contains a with CallState child node, that can be "Active" or "Hold".
-   &lt;Stream&gt; - Audio streams. The &lt;Stream&gt; node contains the following child nodes.

    &lt;HWID- The hardware ID (hw-id) of the resource consumer as specified in the driver’s INF file.

    &lt;TopologyName&gt; - The topology filter reference string of the resource consumer.

    &lt;PinId&gt; - The pin ID of the resource consumer.

    &lt;Mode&gt; - The GUID of the associated mode. For more information, see [Audio Signal Processing Modes](audio-signal-processing-modes.md).

    &lt;ConnectorType&gt; - The connector type of the resource consumer. Valid values are: Host, Loopback, or Offload.

-   &lt;FM&gt; - FM Radio.
-   &lt;KeywordDetector&gt; - Keyword detector used to support Cortana voice interactions.

The following table summarizes the render audio stream priorities, listed from highest to lowest priority.

|                          |     |
|--------------------------|-----|
| Communications           | 1   |
| Game Chat                | 2   |
| Screen Reader            | 3   |
| Camera Shutter           | 4   |
| Push To Talk             | 5   |
| In Call Notification     | 6   |
| Personal Assistant       | 6   |
| Speech                   | 7   |
| Ringtone                 | 8   |
| Alarm                    | 9   |
| Movie                    | 10  |
| Foreground Only Media    | 10  |
| Background Capable Media | 11  |
| Media                    | 11  |
| Sound Effects            | 12  |
| DTMF                     | 12  |
| Game Media               | 12  |
| System                   | 12  |
| Game Effects             | 12  |
| Other                    | 13  |
| Alerts                   | 14  |

 

The following table summarizes the capture audio stream priorities, listed from highest to lowest priority.

|                          |     |
|--------------------------|-----|
| Communications           | 1   |
| Game Chat                | 2   |
| Push To Talk             | 4   |
| Personal Assistant       | 6   |
| Speech                   | 7   |
| Background Capable Media | 8   |
| Media                    | 8   |
| Other                    | 13  |
| Game Media               | 15  |
| Screen Reader            | 15  |
| Alerts                   | 15  |
| Foreground Only Media    | 15  |
| Game Effects             | 15  |
| Sound Effects            | 15  |
| DTMF                     | 15  |
| In Call Notification     | 15  |
| Alarm                    | 15  |
| Camera Shutter           | 15  |
| Movie                    | 15  |
| Ringtone                 | 15  |
| System                   | 15  |

 

**Examples**

- Example 1: The user is talking over Skype, using Communications Render and Capture streams. They start a game, which attempts to create a Game Effects stream. If there aren’t enough resources available, the Game Effects stream creation will fail.

- Example 2: The user is playing music. They start an application that creates a Speech stream. If there aren’t enough resources available, the music stream will be terminated and the Speech stream creation will succeed.

## <span id="Registry_Key_Configuration"></span><span id="registry_key_configuration"></span><span id="REGISTRY_KEY_CONFIGURATION"></span>Registry Key Configuration

The full path to the concurrency constraints XML file needs to be specified in the following registry key. 

```inf
HKR\SYSTEM\MultiMedia\DeviceCapability\ResourceSettings\XMLConfig
```

The path is relative to the driver install. In the driver INF installation the constraint XML file needs to be copied and the following line would be added to register it with the system:

```inf
HKR,SYSTEM\MultiMedia\DeviceCapability\ResourceSettings\XMLConfig,<Name of the constraint>,,<Path to the constraint>
```

In this registry key, provide a value containing the path to the XML. It is recommended that the name of the XML file and regkey value name be unique since there is potential for other subsystems/audio devices providing their own set of constraints in XML files. The regkey can be set in the audio driver INF file.


## <span id="Example_XML_Constraints_File"></span><span id="example_xml_constraints_file"></span><span id="EXAMPLE_XML_CONSTRAINTS_FILE"></span>Example XML Constraints File


This is an example XML constraints file from the SYSVAD virtual audio driver sample.

```xml
<?xml version="1.0" encoding="utf-8"?>
<ConstraintModel>

  <Limits>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>3</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>2</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>2</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneLoopback</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>127</Consumption>
    </Resource>
  </Limits>

  <ExclusiveEndpoints>
    <Endpoint>
      <HWID>Root\sysvad_PhoneAudioSample</HWID>
      <!-- Example of h/w id specified in phoneaudiosample.inf -->
      <TopologyName>TopologySpeaker</TopologyName>
      <!-- Topology filter reference string-->
      <PinId>1</PinId>
      <!-- KSPIN_TOPO_LINEOUT_DEST -->
    </Endpoint>
    <Endpoint>
      <!-- Example of h/w id specified in phoneaudiosample.inf -->
      <HWID>Root\sysvad_PhoneAudioSample</HWID>
      <!-- Topology filter reference string-->
      <TopologyName>TopologyHandsetSpeaker</TopologyName>
      <!-- KSPIN_TOPO_LINEOUT_DEST -->
      <PinId>1</PinId>
    </Endpoint>
  </ExclusiveEndpoints>

  <ResourceConsumer>
    <!-- Phone call -->
    <ConsumerInfo>
      <PhoneCall>
        <CallState>Active</CallState>
      </PhoneCall>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>2</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneLoopback</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>26</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- FM -->
    <ConsumerInfo>
      <FM />
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- Keyword Detector -->
    <ConsumerInfo>
      <KeywordDetector />
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <!--Signal processing mode default-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, Communications mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{98951333-B9CD-48B1-A0A3-FF40682D73F7}</Mode>
        <!--Signal processing mode Communications-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, Speech mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{FC1CFC9B-B9D6-4CFA-B5E0-4BB2166878B2}</Mode>
        <!--Signal processing mode Speech-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, Notification mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{9CF2A70B-F377-403B-BD6B-360863E0355C}</Mode>
        <!--Signal processing mode Notification-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, Media mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{4780004E-7133-41D8-8C74-660DADD2C0EE}</Mode>
        <!--Signal processing mode Media-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, Movie mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{B26FEB0D-EC94-477C-9494-D1AB8E753F6E}</Mode>
        <!--Signal processing mode Movie-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <!--Signal processing mode raw-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, default mode, offload -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <!--Signal processing mode default-->
        <ConnectorType>Offload</ConnectorType>
        <!-- Offload -->
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, Media mode, Offload -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{4780004E-7133-41D8-8C74-660DADD2C0EE}</Mode>
        <!--Signal processing mode Media-->
        <ConnectorType>Offload</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to speaker, Movie mode, offload -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{B26FEB0D-EC94-477C-9494-D1AB8E753F6E}</Mode>
        <!--Signal processing mode Movie-->
        <ConnectorType>Offload</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>


  <ResourceConsumer>
    <!-- AudioStream to speaker, default mode, loopback -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <!--Signal processing mode default-->
        <ConnectorType>Loopback</ConnectorType>
        <!-- Loopback -->
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneLoopback</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, Communications mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{98951333-B9CD-48B1-A0A3-FF40682D73F7}</Mode>
        <!--Signal processing mode Communications-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, Speech mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{FC1CFC9B-B9D6-4CFA-B5E0-4BB2166878B2}</Mode>
        <!--Signal processing mode Speech-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, Notification mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{9CF2A70B-F377-403B-BD6B-360863E0355C}</Mode>
        <!--Signal processing mode Notification-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, Media mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{4780004E-7133-41D8-8C74-660DADD2C0EE}</Mode>
        <!--Signal processing mode Media-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, Movie mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{B26FEB0D-EC94-477C-9494-D1AB8E753F6E}</Mode>
        <!--Signal processing mode Movie-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, default mode, offload -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <!-- Offload -->
        <ConnectorType>Offload</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, Media mode, Offload -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{4780004E-7133-41D8-8C74-660DADD2C0EE}</Mode>
        <!--Signal processing mode Media-->
        <ConnectorType>Offload</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to wired headset, Movie mode, offload -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{B26FEB0D-EC94-477C-9494-D1AB8E753F6E}</Mode>
        <!--Signal processing mode Movie-->
        <ConnectorType>Offload</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>


  <ResourceConsumer>
    <!-- AudioStream to wired headset, default mode, loopback -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologySpeakerHeadset</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <!-- Loopback -->
        <ConnectorType>Loopback</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneLoopback</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to BT speaker, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyBthHfpSpeaker</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to BT speaker, raw mode, offload -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyBthHfpSpeaker</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <!-- Offload -->
        <ConnectorType>Offload</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxTwoOffload</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to BT speaker, default mode, loopback -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyBthHfpSpeaker</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <!-- Loopback -->
        <ConnectorType>Loopback</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneLoopback</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to handset speaker, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetSpeaker</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to handset speaker, Communications mode, host -->
    <ConsumerInfo>
      <Stream>
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <TopologyName>TopologyHandsetSpeaker</TopologyName>
        <!-- Topology filter reference string-->
        <PinId>1</PinId>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <Mode>{98951333-B9CD-48B1-A0A3-FF40682D73F7}</Mode>
        <!--Signal processing mode Communications-->
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to handset speaker, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetSpeaker</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream to handset speaker, default mode, loopback -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetSpeaker</TopologyName>
        <!-- KSPIN_TOPO_LINEOUT_DEST -->
        <PinId>1</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <!-- Loopback -->
        <ConnectorType>Loopback</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxThreeRender</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneLoopback</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicIn</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic, communications mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicIn</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode communications-->
        <Mode>{98951333-B9CD-48B1-A0A3-FF40682D73F7}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic, speech mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicIn</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode speech-->
        <Mode>{FC1CFC9B-B9D6-4CFA-B5E0-4BB2166878B2}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic, notification mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicIn</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode notification-->
        <Mode>{9CF2A70B-F377-403B-BD6B-360863E0355C}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicIn</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from wired headset mic, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicHeadset</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from wired headset mic, communications mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicHeadset</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode communications-->
        <Mode>{98951333-B9CD-48B1-A0A3-FF40682D73F7}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from wired headset mic, speech mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicHeadset</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode speech-->
        <Mode>{FC1CFC9B-B9D6-4CFA-B5E0-4BB2166878B2}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from wired headset mic, notification mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicHeadset</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode notification-->
        <Mode>{9CF2A70B-F377-403B-BD6B-360863E0355C}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from wired headset mic, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicHeadset</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic array, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicArray1</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic array, communications mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicArray1</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode communications-->
        <Mode>{98951333-B9CD-48B1-A0A3-FF40682D73F7}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic array, speech mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicArray1</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode speech-->
        <Mode>{FC1CFC9B-B9D6-4CFA-B5E0-4BB2166878B2}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic array, notification mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicArray1</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode notification-->
        <Mode>{9CF2A70B-F377-403B-BD6B-360863E0355C}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from mic array, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyMicArray1</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from BT mic, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyBthHfpMic</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from BT mic, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyBthHfpMic</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from handset mic, default mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetMic</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode default-->
        <Mode>{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from handset mic, communications mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetMic</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode communications-->
        <Mode>{98951333-B9CD-48B1-A0A3-FF40682D73F7}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from handset mic, speech mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetMic</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode speech-->
        <Mode>{FC1CFC9B-B9D6-4CFA-B5E0-4BB2166878B2}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from handset mic, notification mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetMic</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode notification-->
        <Mode>{9CF2A70B-F377-403B-BD6B-360863E0355C}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>2</Consumption>
    </Resource>
  </ResourceConsumer>

  <ResourceConsumer>
    <!-- AudioStream from handset mic, raw mode, host -->
    <ConsumerInfo>
      <Stream>
        <!-- Example of h/w id specified in phoneaudiosample.inf -->
        <HWID>Root\sysvad_PhoneAudioSample</HWID>
        <!-- Topology filter reference string-->
        <TopologyName>TopologyHandsetMic</TopologyName>
        <!-- KSPIN_TOPO_MIC_ELEMENTS -->
        <PinId>0</PinId>
        <!--Signal processing mode raw-->
        <Mode>{9E90EA20-B493-4FD1-A1A8-7E1361A956CF}</Mode>
        <ConnectorType>Host</ConnectorType>
      </Stream>
    </ConsumerInfo>
    <Resource>
      <ID>MaxTwoCapture</ID>
      <Consumption>1</Consumption>
    </Resource>
    <Resource>
      <ID>MaxOneRawStreamInPhoneCall</ID>
      <Consumption>1</Consumption>
    </Resource>
  </ResourceConsumer>

</ConstraintModel>
```

 

 




