const video_input = document.getElementById('id_video')
const timezone_input = document.getElementById('id_timezone')
const days = document.getElementById('id_day')
const month = document.getElementById('id_month')
const year_select = document.getElementById('id_year')


//disable the first options for all inputs
const disableFirstOption = () => {
    form = document.getElementById('tiktok-upload-form')
    elements = Array.from(form.elements)
    console.log(elements)
    elements.forEach(el => {
        if(el.type === 'select-one'){
            el.options[0].disabled = true
        }
    })
}

disableFirstOption()


// set users current timezone for processing on backend
const date = new Date()
let year = date.getFullYear()

const setTimeZone = () => {
    const tz = date.toLocaleTimeString('en-us', {timeZoneName:'short'}).split(' ')[2]
    console.log(tz)
    timezone_input.value = tz
}

setTimeZone()



const day_map_31 = [1,3,5,7,8,10,12]
const day_map_30 = [4,6,9,11]
const feb = () => {
    if(year % 400 === 0){
        return 29
    }
    return 28
}


//Set options for days in the month user can select from
const setDays = () => {
    let days_list = 0
    const set_month = parseInt(month.value)

    if(set_month === 2){
        days_list = feb()
    }
    else if(day_map_31.includes(set_month)){
        days_list = 31
    }
    else if(day_map_30.includes(set_month)){
        days_list = 30
    }

    for(let i = 2; i < days_list + 1; i++){
        let day = i.toString()
        const opt = document.createElement('option')
        opt.value = day
        opt.innerHTML = day
        days.appendChild(opt)
    }

}


month.addEventListener('change', setDays)


//handle edge case for leap year selection
const leapYearEdgeCase = (e) => {
    const selectedYear = parseInt(e.target.value)
    if(selectedYear !== year){
        year = selectedYear
        if(year % 400 === 0){
            let day_select = document.getElementById('id_day')
            let selected_month = document.getElementById('id_month')
            let month_index = selected_month.options.selectedIndex
            if(parseInt(selected_month.options[month_index].value) === 2 ){
                day_select.options.selectedIndex = 0
                setDays()
            }
        }
    }
}

year_select.addEventListener('change', leapYearEdgeCase)
