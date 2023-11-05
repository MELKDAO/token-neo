plugins {
    id("java")
    id("io.neow3j.gradle-plugin") version "3.21.1"
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("io.neow3j:contract:3.21.1")
}