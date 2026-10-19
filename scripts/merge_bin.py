# После сборки склеивает bootloader, таблицу разделов и прошивку в один
# merged.bin, который шьётся целиком по адресу 0x0 (например, через esptool-js).
Import("env")


def merge_bin(source, target, env):
    images = env.Flatten(env.get("FLASH_EXTRA_IMAGES", []))
    images += ["$ESP32_APP_OFFSET", "$BUILD_DIR/${PROGNAME}.bin"]
    env.Execute(" ".join([
        '"$PYTHONEXE"', '"$OBJCOPY"',
        "--chip", env.BoardConfig().get("build.mcu"),
        "merge_bin", "-o", "$BUILD_DIR/merged.bin",
    ] + images))


env.AddPostAction("$BUILD_DIR/${PROGNAME}.bin", merge_bin)
