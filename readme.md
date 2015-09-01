Krabby Patty
============
* Install python and kivy
* Create your kivy application. My kivy application only consists of `main.py` and `rand.kv`
* Run `buildozer init`
* Run `buildozer -v android release` or `buildozer -v android debug` to debug
* Sign your app

    - Generate a private key using keytool. For example:
        ```
        $ keytool -genkey -v -keystore my-release-key.keystore
        -alias alias_name -keyalg RSA -keysize 2048 -validity 10000
        ```
        This example prompts you for passwords for the keystore and key, and to provide the Distinguished Name fields for your key. It then generates the keystore as a file called my-release-key.keystore. The keystore contains a single key, valid for 10000 days. The alias is a name that you will use later when signing your app.

    - Sign your app with your private key using jarsigner:
        ```
        $ jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1
        -keystore my-release-key.keystore my_application.apk alias_name
        ```

    - Verify that your APK is signed. For example:
        ```
        $ jarsigner -verify -verbose -certs my_application.apk
        ```

    - Align the final APK package using zipalign.
        ```
        $ zipalign -v 4 your_project_name-unaligned.apk your_project_name.apk
        ```