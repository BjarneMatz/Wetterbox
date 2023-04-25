//libraries
#include <DHT_U.h>
#include <DHT.h>


//sensor reading variables
int water_level = 0;
int sun_intensity = 0;
int rain_intensity = 0;
int sound_intensity = 0;

int earth_temperature = 0;
int ground_temperature = 0;
int system_temperature = 0;


//sensor pins
const int water_level_sensor = 2;
const int sun_intensity_sensor = 3;
const int rain_intensity_sensor = 4;
const int sound_intensity_sensor = 5;

const int earth_temperature_sensor = 6;
const int ground_temperature_sensor = 7;
const int system_temperature_sensor = 8;


//dht sensor setup
#define DHTPIN 25
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);


//led pins
const int activity_led = 9;
const int heart_beat_led = 10;
const int error_led = 11;

//buzzer pin
const int buzzer = 12;

void setup(){
    //sensor setup
    pinMode(water_level_sensor, INPUT);
    pinMode(sun_intensity_sensor, INPUT);
    pinMode(rain_intensity_sensor, INPUT);
    pinMode(sound_intensity_sensor, INPUT);
    
    pinMode(earth_temperature_sensor, INPUT);
    pinMode(ground_temperature_sensor, INPUT);
    pinMode(system_temperature_sensor, INPUT);
    
    //led setup
    pinMode(activity_led, OUTPUT);
    pinMode(heart_beat_led, OUTPUT);
    pinMode(error_led, OUTPUT);
    
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
    
    //deactivate buzzer and error led
    digitalWrite(buzzer,LOW);
    digitalWrite(error_led,LOW);
}

void loop(){
    read_sensors();
    serial_to_raspberry();
    heart_beat();
}

void serial_to_raspberry(){
    Serial.print("water_level: ");
    Serial.print(water_level);
    Serial.print(" sun_intensity: ");
    Serial.print(sun_intensity);
    Serial.print(" rain_intensity: ");
    Serial.print(rain_intensity);
    Serial.print(" sound_intensity: ");
    Serial.print(sound_intensity);
    Serial.print(" earth_temperature: ");
    Serial.print(earth_temperature);
    Serial.print(" ground_temperature: ");
    Serial.print(ground_temperature);
    Serial.print(" system_temperature: ");
    Serial.print(system_temperature);
    Serial.println();
}

void read_sensors(){
    water_level = analogRead(water_level_sensor);
    sun_intensity = analogRead(sun_intensity_sensor);
    rain_intensity = analogRead(rain_intensity_sensor);
    sound_intensity = analogRead(sound_intensity_sensor);
    
    earth_temperature = analogRead(earth_temperature_sensor);
    ground_temperature = analogRead(ground_temperature_sensor);
    system_temperature = analogRead(system_temperature_sensor);
}


void heart_beat(){
    digitalWrite(heart_beat_led, HIGH);
    delay(100);
    digitalWrite(heart_beat_led, LOW);
    delay(100);
}