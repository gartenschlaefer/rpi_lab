// --
// lcd ili934 on korvo 2 example - academic ai generated

#include "bsp/esp-bsp.h"
#include "lvgl.h"
#include "esp_log.h"
#include "esp_err.h"

static const char *TAG = "korvo2_display";


void app_main(void)
{
    // Initialize the board and start the display + LVGL
    bsp_display_start();

    // Optional: turn backlight on (some BSPs do this in bsp_display_start)
    bsp_display_backlight_on();

    // create a simple LVGL label, use BSP display lock for thread safety when modifying LVGL objects
    bsp_display_lock(0);
    lv_obj_t *label = lv_label_create(lv_scr_act());
    lv_label_set_text(label, "Hello, ESP32-S3-Korvo-2!");
    lv_obj_center(label);
    bsp_display_unlock();

    // end text
    ESP_LOGI(TAG, "Display example started.");
}