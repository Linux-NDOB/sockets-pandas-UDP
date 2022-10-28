<template>
    <v-sheet color="red">
        <v-container class="pa-0">
            <v-app-bar
                    dense
                    flat
                    color="blue accent-4"
            >
                <v-btn icon>
                    <v-icon>mdi-home-outline</v-icon>
                </v-btn>
                <v-divider inset vertical></v-divider>

                <v-btn text :key="item.id" v-for="item in quickLinks" v-text="item.text"></v-btn>
                <v-spacer></v-spacer>
                <v-btn text v-text="'Sign In'"></v-btn>
                <v-btn text v-text="'Register'"></v-btn>
            </v-app-bar>
        </v-container>
    </v-sheet>
</template>
