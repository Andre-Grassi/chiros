import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 200
    visible: true
    title: "Chiros"
    visibility: Window.Maximized

    readonly property list<string> texts: ["Hallo Welt", "Hei maailma",
                                           "Hola Mundo", "Привет мир"]

    function setText() {
        var i = Math.round(Math.random() * 3)
        text.text = texts[i]
    }

    Rectangle {
        anchors.fill: parent
        color: "blue"
    }
}