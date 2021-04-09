---
title: PnPUtil Examples
description: PnPUtil Examples
ms.date: 01/31/2018
ms.localizationpriority: medium
---

# PnPUtil Examples

This topic provides examples on how to use the PnPUtil tool.

<dl>
  <dt>Add driver package</dt>
  <dd><pre><code>pnputil /add-driver x:\driver.inf                                  </code></pre></dd>
  <dt>Add multiple driver packages</dt>
  <dd><pre><code>pnputil /add-driver c:\oem\*.inf                                   </code></pre></dd>
  <dt>Add and install driver package</dt>
  <dd><pre><code>pnputil /add-driver device.inf /install                            </code></pre></dd>
  <dt>Enumerate OEM driver packages</dt>
  <dd><pre><code>pnputil /enum-drivers                                              </code></pre></dd>
  <dt>Delete driver package</dt>
  <dd><pre><code>pnputil /delete-driver oem0.inf                                    </code></pre></dd>
  <dt>Force delete driver package</dt>
  <dd><pre><code>pnputil /delete-driver oem1.inf /force                             </code></pre></dd>
  <dt>Export driver package</dt>
  <dd><pre><code>pnputil /export-driver oem6.inf .                                  </code></pre></dd>
  <dt>Export all driver packages</dt>
  <dd><pre><code>pnputil /export-driver * c:\backup                                 </code></pre></dd>
  <dt>Disables device specified by device instance ID</dt>
  <dd><pre><code>pnputil /disable-device "USB\VID_045E&PID_00DB\6&870CE29&0&1"      </code></pre></dd>
  <dt>Enables device specified by device instance ID</dt>
  <dd><pre><code>pnputil /enable-device "USB\VID_045E&PID_00DB\6&870CE29&0&1"       </code></pre></dd>
  <dt>Restarts device specified by device instance ID</dt>
  <dd><pre><code>pnputil /restart-device "USB\VID_045E&PID_00DB\6&870CE29&0&1"      </code></pre></dd>
  <dt>Removes device specified by device instance ID</dt>
  <dd><pre><code>pnputil /remove-device "USB\VID_045E&PID_00DB\6&870CE29&0&1"       </code></pre></dd>
  <dt>Scan the system for any device hardware changes</dt>
  <dd><pre><code>pnputil /scan-devices                                              </code></pre></dd>
  <dt>Enumerate only connected devices on the system</dt>
  <dd><pre><code>pnputil /enum-devices /connected                                   </code></pre></dd>
  <dt>Enumerate device with specific instance ID</dt>
  <dd><pre><code>pnputil /enum-devices /instanceid "ACPI\PNP0A08\1"                 </code></pre></dd>
  <dt>Enumerate all devices with specific class</dt>
  <dd><pre><code>pnputil /enum-devices /class Display                               </code></pre></dd>
  <dt>Enumerate all devices with specific problem code</dt>
  <dd><pre><code>pnputil /enum-devices /problem 28                                  </code></pre></dd>
  <dt>Enumerate all devices with problems and display hardware/compatible IDs</dt>
  <dd><pre><code>pnputil /enum-devices /problem /ids                                </code></pre></dd>
  <dt>Enumerate only enabled interfaces on the system</dt>
  <dd><pre><code>pnputil /enum-interfaces /enabled                                  </code></pre></dd>
</dl>


 

 





