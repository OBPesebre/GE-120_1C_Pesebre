import React from 'react'
import { Picker } from '@react-native-picker/picker';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, TextInput, View, Button} from 'react-native';

export default function App() {

  const [value, onChangeValue] = React.useState('---');
  const [inputValue, onChangeinputValue] = React.useState('Input value here:');
  const [inputCase,setInputCase] = React.useState ("Select case");

  function convertValue(value){
    /*
    Calculates DMS to DD and vice versa

    Input:
    DMS/DD - string

    Output
    DMS/DD - float
    */
    
    if (inputCase == "1") {
      var degrees = Math.floor(value)
      var minutes = Math.floor((value - degrees)*60)
      var seconds = Math.round((value - degrees - (minutes/60))*3600)
  
      var output = degrees.toString().concat("-", minutes.toString(), "-", seconds.toString())
      onChangeValue(output)
    }
   
    else {
      var elements = value.split("-")
      var output = parseFloat(elements[0]) + parseFloat(elements[1]/60) + parseFloat(elements[2]/3600)
      onChangeValue(output)
    }
}
  return (
    <View style={styles.box}>
      <View style={styles.box_1}>
        <Text style={styles.titleText}>DMS-DD CONVERTER!</Text>
      </View>
      
      <View style={styles.box_2}>
        <View style={styles.box_2A}>
          <Text style={styles.case_design}>Input case</Text>
          <Picker
            selectedValue={inputCase}
            onValueChange={(itemValue, itemIndex) =>
              setInputCase(itemValue)
            }>
            <Picker.Item label="DD to DMS" value="1" />
            <Picker.Item label="DMS to DD" value="2" />
          </Picker>
        </View>

        <View style={styles.box_2B}>
        <TextInput
        style={styles.input}
        onChangeText={onChangeinputValue}
        value={inputValue}
      />
       <Button
      title="Convert"
      onPress={() => convertValue(inputValue)}
      /> 
        </View>
      </View>

      <View style={styles.box_3}>
      <View style={styles.box_3A}>
        <Text style={styles.result_box}>Result:</Text>
        <Text style={styles.result_box}>{value}</Text>
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
  box_2A: {
    flexDirection: 'column',
    backgroundColor: '#FFF6CC',
    width: '100%',
    height: '50%',
    padding: 10
  },
  case_design: {
    fontSize: 24,
    fontWeight: '200',
    fontFamily: 'serif',
    alignItems: 'center',
    justifyContent: 'center',
    color: 'black'
  },
  box_2B: {
    flex: 1,
    backgroundColor: '#FFF6CC',
    width: '100%',
    height: '50%'
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