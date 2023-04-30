//libraries to include
#include <DHT_U.h>
#include <DHT.h>
#include <DallasTemperature.h>
#include <OneWire.h>

//sensor reading variables
int water_level = 0;
int sun_intensity = 0;
int rain_intensity = 0;
int sound_intensity = 0;

float earth_temperature = 0;
float ground_temperature = 0;
float system_temperature = 0;

float dht_humidity = 0;
float dht_temperature = 0;
float dht_heat_index = 0;


//sensor pinout (analog)
const int water_level_sensor = A1;
const int sun_intensity_sensor = A2;
const int rain_intensity_sensor = A0;
const int sound_intensity_sensor = A3;

//sensor pinout (digital)
#define earth_temperature_sensor_pin 7
#define ground_temperature_sensor_pin 8
#define system_temperature_sensor_pin 9

OneWire earth_temperature_sensor_onewire(earth_temperature_sensor_pin);
OneWire ground_temperature_sensor_onewire(ground_temperature_sensor_pin);
OneWire system_temperature_sensor_onewire(system_temperature_sensor_pin);

DallasTemperature earth_temperature_sensor(&earth_temperature_sensor_onewire);
DallasTemperature ground_temperature_sensor(&ground_temperature_sensor_onewire);
DallasTemperature system_temperature_sensor(&earth_temperature_sensor_onewire); 


//dht sensor setup
#define DHTPIN 25
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);


//led pinout
const int activity_led = 2;
const int heart_beat_led = 3;
const int error_led = 5;
const int reading_led = 4;

//buzzer pin
const int buzzer = 6;

//master delay
const int master_delay = 5000;

void setup(){
    //sensor setup (analog)
    pinMode(water_level_sensor, INPUT);
    pinMode(sun_intensity_sensor, INPUT);
    pinMode(rain_intensity_sensor, INPUT);
    pinMode(sound_intensity_sensor, INPUT);
    
    
    //led setup
    pinMode(activity_led, OUTPUT);
    pinMode(heart_beat_led, OUTPUT);
    pinMode(error_led, OUTPUT);
    pinMode(reading_led, OUTPUT);
    
    //buzzer setup
    pinMode(buzzer, OUTPUT);
    
    //activate buzzer (until raspberry pi is connected and digital sensors are initialized)
    digitalWrite(buzzer,HIGH);

    //dht sensor setup
    dht.begin();
    
    //activate error led until raspberry pi is connected
    digitalWrite(error_led,HIGH);

    //serial setup
    Serial.begin(9600);
    while (!Serial) {
        ; // wait for raspberry pi to connect
    }
    
    delay(250);
    //deactivate buzzer and error led
    digitalWrite(buzzer,LOW);
    digitalWrite(error_led,LOW);

    //wait for raspberry pi to initialize
    delay(5000);

    //activate activity led
    digitalWrite(activity_led,HIGH);

}

void loop(){
    read_sensors();
    serial_to_raspberry();
    check_if_raspberry_is_connected();
    heart_beat();
}

void serial_to_raspberry(){

    //dht sensor data
    Serial.print(dht_humidity);
    Serial.print(",");
    Serial.print(dht_temperature);
    Serial.print(",");
    Serial.print(dht_heat_index);
    Serial.print(",");

    //digital sensor data
    Serial.print(earth_temperature);
    Serial.print(",");
    Serial.print(ground_temperature);
    Serial.print(",");
    Serial.print(system_temperature);
    Serial.print(",");

    //analog sensor data
    Serial.print(water_level);
    Serial.print(",");
    Serial.print(sun_intensity);
    Serial.print(",");
    Serial.print(rain_intensity);
    Serial.print(",");
    Serial.print(sound_intensity);
    Serial.print(",");

    //impossible value to indicate end of data
    Serial.println("1111"); 
}

void check_if_raspberry_is_connected(){
    
    //if raspberry pi is not connected, activate error led and buzzer
    if(!Serial.available()){
        digitalWrite(error_led,HIGH);
        //digitalWrite(buzzer,HIGH);
    }
    else{
        digitalWrite(error_led,LOW);
        //digitalWrite(buzzer,LOW);
    }
    
    Serial.read();
}

void read_sensors(){
   //turn on reading led to indicate sensor reading
    digitalWrite(reading_led, HIGH);

    //read digital sensors
    earth_temperature_sensor.requestTemperatures();
    ground_temperature_sensor.requestTemperatures();
    system_temperature_sensor.requestTemperatures();

    earth_temperature = earth_temperature_sensor.getTempCByIndex(0);
    ground_temperature = ground_temperature_sensor.getTempCByIndex(0);
    system_temperature = system_temperature_sensor.getTempCByIndex(0);


    //read dht sensor
    dht_humidity = dht.readHumidity();
    dht_temperature = dht.readTemperature();
    dht_heat_index = dht.computeHeatIndex(dht_temperature, dht_humidity, false);

    //read analog sensors
    water_level = analogRead(water_level_sensor);
    sun_intensity = analogRead(sun_intensity_sensor);
    rain_intensity = analogRead(rain_intensity_sensor);
    sound_intensity = analogRead(sound_intensity_sensor);
    
    
    //turn off reading led
    digitalWrite(reading_led, LOW);
}


void heart_beat(){
    //function to indicate that arduino is running properly

    digitalWrite(heart_beat_led, HIGH);
    delay(master_delay/2);
    digitalWrite(heart_beat_led, LOW);
    delay(master_delay/2);
}