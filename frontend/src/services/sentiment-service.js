import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/analyze/'

const postText = async (text, model) => {
  try {
    const response = await axios.post(API_URL, { text, model })
    return response.data
  } catch (error) {
    console.error('Error analyzing sentiment:', error)
    return { error: 'Failed to analyze sentiment' }
  }
}

export default postText
