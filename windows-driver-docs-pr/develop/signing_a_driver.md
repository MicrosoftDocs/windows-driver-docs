Signing a Driver
============================================================

All drivers running on 64-bit versions of Windows must be signed before Windows will load them. However, driver signing is not required on 32-bit versions of Windows.

In order to sign a driver, a certificate is required. You can create your own certificate to sign your driver with during development and testing. However, for a public release you must sign your driver with a certificate issued by a trusted root authority.

**Note**  A *driver package project* can package the output of other projects. If you build a driver package project, Microsoft Visual Studio will build the other projects on which it has dependencies. The driver package project has its own driver signing properties that are separate from any other dependent projects, and its driver signing properties apply *only* to the catalog (if any) produced by the driver package project. That is, the driver package project will not automatically add an embedded signature to driver binaries produced by other projects, as a different certificate may be used to sign the other driver projects, for example, a test certificate, and the result in such a case would be a driver package where the binaries are unintentionally signed with one certificate, while the package catalog is signed with a different certificate. This can result in performance degradation. For example, if a boot start driver binary's embedded signature is invalid, Windows cannot use certificate it was signed with to validate the binary. Instead, Windows must validate the binary against the catalog's signature, which would increase boot time.

 

This section describes how to use Visual Studio to sign a driver package.

-   [Signing a Driver During Development and Testing](signing_a_driver_during_development_and_testing.md)
-   [Signing a Driver for Public Release](signing_a_driver_for_public_release.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Signing%20a%20Driver%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


