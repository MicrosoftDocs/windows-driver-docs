---
title: Device Manager Error Messages
description: Device Manager Error Messages
ms.assetid: 38958790-6b60-48ff-a341-fc39a16602ab
keywords:
- Device Manager WDK , errors
- errors WDK Device Manager
- yellow exclamation point WDK Device Manager
- messages WDK Device Manager
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Device Manager Error Messages


## <a href="" id="ddk-device-manager-error-messages-dg"></a>


When Device Manager marks a device with a yellow exclamation point, it also provides an error message.

The following table lists the errors reported by Device Manager on Windows 2000 and later versions of Windows. These error codes are defined in Cfg.h.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Error code</th>
<th align="left">Problem name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Code 1</p></td>
<td align="left"><p>[CM_PROB_NOT_CONFIGURED](cm-prob-not-configured.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 3</p></td>
<td align="left"><p>[CM_PROB_OUT_OF_MEMORY](cm-prob-out-of-memory.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 9</p></td>
<td align="left"><p>[CM_PROB_INVALID_DATA](cm-prob-invalid-data.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 10</p></td>
<td align="left"><p>[CM_PROB_FAILED_START](cm-prob-failed-start.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 12</p></td>
<td align="left"><p>[CM_PROB_NORMAL_CONFLICT](cm-prob-normal-conflict.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 14</p></td>
<td align="left"><p>[CM_PROB_NEED_RESTART](cm-prob-need-restart.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 16</p></td>
<td align="left"><p>[CM_PROB_PARTIAL_LOG_CONF](cm-prob-partial-log-conf.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 18</p></td>
<td align="left"><p>[CM_PROB_REINSTALL](cm-prob-reinstall.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 19</p></td>
<td align="left"><p>[CM_PROB_REGISTRY](cm-prob-registry.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 21</p></td>
<td align="left"><p>[CM_PROB_WILL_BE_REMOVED](cm-prob-will-be-removed.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 22</p></td>
<td align="left"><p>[CM_PROB_DISABLED](cm-prob-disabled.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 24</p></td>
<td align="left"><p>[CM_PROB_DEVICE_NOT_THERE](cm-prob-device-not-there.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 28</p></td>
<td align="left"><p>[CM_PROB_FAILED_INSTALL](cm-prob-failed-install.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 29</p></td>
<td align="left"><p>[CM_PROB_HARDWARE_DISABLED](cm-prob-hardware-disabled.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 31</p></td>
<td align="left"><p>[CM_PROB_FAILED_ADD](cm-prob-failed-add.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 32</p></td>
<td align="left"><p>[CM_PROB_DISABLED_SERVICE](cm-prob-disabled-service.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 33</p></td>
<td align="left"><p>[CM_PROB_TRANSLATION_FAILED](cm-prob-translation-failed.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 34</p></td>
<td align="left"><p>[CM_PROB_NO_SOFTCONFIG](cm-prob-no-softconfig.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 35</p></td>
<td align="left"><p>[CM_PROB_BIOS_TABLE](cm-prob-bios-table.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 36</p></td>
<td align="left"><p>[CM_PROB_IRQ_TRANSLATION_FAILED](cm-prob-irq-translation-failed.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 37</p></td>
<td align="left"><p>[CM_PROB_FAILED_DRIVER_ENTRY](cm-prob-failed-driver-entry.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 38</p></td>
<td align="left"><p>[CM_PROB_DRIVER_FAILED_PRIOR_UNLOAD](cm-prob-driver-failed-prior-unload.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 39</p></td>
<td align="left"><p>[CM_PROB_DRIVER_FAILED_LOAD](cm-prob-driver-failed-load.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 40</p></td>
<td align="left"><p>[CM_PROB_DRIVER_SERVICE_KEY_INVALID](cm-prob-driver-service-key-invalid.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 41</p></td>
<td align="left"><p>[CM_PROB_LEGACY_SERVICE_NO_DEVICES](cm-prob-legacy-service-no-devices.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 42</p></td>
<td align="left"><p>[CM_PROB_DUPLICATE_DEVICE](cm-prob-duplicate-device.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 43</p></td>
<td align="left"><p>[CM_PROB_FAILED_POST_START](cm-prob-failed-post-start.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 44</p></td>
<td align="left"><p>[CM_PROB_HALTED](cm-prob-halted.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 45</p></td>
<td align="left"><p>[CM_PROB_PHANTOM](cm-prob-phantom.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 46</p></td>
<td align="left"><p>[CM_PROB_SYSTEM_SHUTDOWN](cm-prob-system-shutdown.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 47</p></td>
<td align="left"><p>[CM_PROB_HELD_FOR_EJECT](cm-prob-held-for-eject.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 48</p></td>
<td align="left"><p>[CM_PROB_DRIVER_BLOCKED](cm-prob-driver-blocked.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 49</p></td>
<td align="left"><p>[CM_PROB_REGISTRY_TOO_LARGE](cm-prob-registry-too-large.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 50</p></td>
<td align="left"><p>[CM_PROB_SETPROPERTIES_FAILED](cm-prob-setproperties-failed.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 51</p></td>
<td align="left"><p>[CM_PROB_WAITING_ON_DEPENDENCY](cm-prob-waiting-on-dependency.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 52</p></td>
<td align="left"><p>[CM_PROB_UNSIGNED_DRIVER](cm-prob-unsigned-driver.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Code 53</p></td>
<td align="left"><p>[CM_PROB_USED_BY_DEBUGGER](cm-prob-used-by-debugger.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code 54</p></td>
<td align="left"><p>[CM_PROB_DEVICE_RESET](cm-prob-device-reset.md)</p></td>
</tr>
</tbody>
</table>

 

 

 





