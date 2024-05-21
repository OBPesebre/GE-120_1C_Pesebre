/*
I will use view to put boxes in my UI that will act as placeholder for other elements. I will use texts to input labels on the app. In addition, I will use text input to
allow the users to input their azimuth. Finally, I will place a button for triggering the conversion of Azimuth to bearing.
*/

import React from 'react'
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, TextInput, View, Button} from 'react-native';



export default function App() {

    const [azimuth, bearing] = React.useState('---');
    const [inputValue, onChangeinputValue] = React.useState('Input value here:');
  
    function convertToBearing(azimuth){
      /*
      Calculates azimuth to bearing and vice versa
  
      Input:
      azimuth - string
  
      Output
      bearing - float
      */
      
    if (azimuth > 0 && azimuth < 90) {
        bearing = 'S '.concat(azimuth.toString(), ' W')
    }
    else if (azimuth > 90 && azimuth < 180) {
        bearing = 'N '.concat(180-azimuth.toString(), ' W')
    }
    else if (azimuth > 180 && azimuth < 270) {
        bearing = 'N '.concat((azimuth-180).toString(), ' E')
    }
    else if (azimuth > 270 && azimuth < 360) {
        bearing = 'S '.concat(360-azimuth.toString(), ' E')
    }
    else if (azimuth == 0) {
        bearing = "DUE SOUTH"
    }
    else if (azimuth == 90) {
        bearing = "DUE WEST"
    }
    else if (azimuth == 180) {
        bearing = "DUE NORTH"
    }
    else if (azimuth == 270) {
        bearing = "DUE EAST"
    }
    else{
        bearing = "NA"
    }
  }
    return (
      <View style={styles.box}>
        <View style={styles.box_1}>
          <Text style={styles.titleText}>Azimuth to Bearing Converter!</Text>
        </View>
        
        <View style={styles.box_2}>
        <TextInput
          style={styles.input}
          onChangeText={onChangeinputValue}
          value={inputValue}
        />
        <Button
        title="Convert"
        onPress={() => convertToBearing(inputValue)}
        />
        </View>
  
        <View style={styles.box_3}>
        <View style={styles.box_3A}>
          <Text style={styles.result_box}>Result:</Text>
          <Text style={styles.result_box}>{azimuth}</Text>
          </View>
        </View>
  
        <View style={styles.box_4}>
        <Text style={styles.titleQuote}>Sometimes, we need to convert things in our lives for us to attain our desires.</Text>
        </View>
      </View>
    );
  }
  
  /*
  The following section contains the designs and layout of each box.
  */
  
  const styles = StyleSheet.create({
    box: {
      flex: 1,
      backgroundColor: '#1d2951',
      alignItems: 'center',
      justifyContent: 'center'
    },
    box_1: {
      width: '100%',
      height: '15%',
      alignItems: 'center',
      justifyContent: 'center'
    },
    titleText: {
      fontSize: 30,
      fontWeight: '600',
      alignItems: 'center',
      justifyContent: 'center',
      fontFamily: 'serif',
      color: "white"
    },
    box_2: {
      width: '100%',
      height: '35%',
      alignItems: 'center',
      justifyContent: 'center',
      padding: 10
    },
    input: {
      height: '50%',
      width: '70%',
      fontSize: 40,
      color: 'black',
      fontFamily: 'serif',
      alignItems: 'center',
      justifyContent: 'center'
    },
    box_3: {
      width: '100%',
      height: '35%',
      padding: 10
    },
    box_3A: {
      flex: 1,
      backgroundColor: '#FFF6CC',
      width: '100%',
      height: '100%',
      alignItems: 'center',
      justifyContent: 'center',
    },
    result_box: {
      fontSize: 50,
      fontWeight: '600',
      fontFamily: 'serif',
      alignItems: 'center',
      justifyContent: 'center',
      color: 'black'
    },
    box_4: {
      width: '100%',
      height: '15%',
      alignItems: 'center',
      justifyContent: 'center',
      padding: 10
    },
    titleQuote: {
      fontSize: 15,
      fontWeight: '600',
      fontFamily: 'serif',
      alignItems: 'center',
      justifyContent: 'center',
      color: 'white'
    },
  });